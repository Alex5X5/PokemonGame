import sqlite3
from typing import Any

from Logic.Models.Trainer import Trainer
from Logic.Services.LoggingService import Logger
from Logic.Services.PathService import PathService


class DbService:

    def __init__(self, path_service:PathService):
        self.__path_service:PathService = path_service
        self.logger:Logger = Logger('DbService')

    @property
    def __path(self) -> str:
        return self.__path_service.assets_path('pokemon_database.sqlite3')

    def __init_connection(self) -> sqlite3.Connection:
        """
            Hilfsfunktion zur Herstellung einer Verbindung mit der SQLite-Datenbank.
            - Überprüft, ob die Datenbankdatei existiert
            - falls die haupt Datenbank nicht existiert, wird nach den beiden fallback-Datenbanken gesucht oder eine Exception geworfen.
            - das row_factory attribut der connection wird auf sqlite3.Row gesetzt, um die Ergebnisse als Dictionaries zurückzugeben.
        """
        con = sqlite3.connect(self.__path)
        con.row_factory = sqlite3.Row
        return con


    def create_trainer(self, trainer:Trainer):
        pass

    def load_trainer(self, trainer_name:str) -> Trainer:
        data:list[dict[str, Any]] = self.execute_raw(f"SELECT * FROM Trainers WHERE Name=\"{trainer_name}\"", expect_result=True)
        return Trainer.from_dictionary(data[0])

    def insert_or_update_trainer(self, trainer:Trainer):
        self.execute_raw(f"INSERT OR IGNORE INTO Trainers WHERE Id={trainer.id} (Name) VALUES ({trainer.name}); UPDATE Trainers SET Name = {trainer.name} WHERE Id={trainer.id}")

    def create_trainer(self, trainer: Trainer) -> None:
        raise NotImplementedError

    def fetch_hardware(self) ->list[dict[str, str]]:
        """
            Ruft alle Hardware-Einträge aus der Tabelle `Hardware` ab.
        """
        try:
            with self.__init_connection() as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Hardware")
                rows = cur.fetchall()
                return [dict(row) for row in rows]
        except sqlite3.Error as e:
            raise RuntimeError(f"Fehler beim Abrufen der Hardware: {e.args[0]}")

    def fetch_hardware_by_id(self, id:int):
        """
            Ruft die Daten einer spezifischen Hardware anhand ihres `Service_Tag` ab.
            :param int id: eine Konstante zum Identifizieren des Datensatzes
        """
        try:
            with self.__init_connection() as con:
                cur = con.cursor()
                # ID muss hier mit einem Komma an Ende übergeben werden, um als Tuple zu agieren
                cur.execute("SELECT * FROM Hardware WHERE ID = ?", (id,))
                row = cur.fetchone()
                return dict(row) if row else None
        except sqlite3.Error as e:
            raise RuntimeError(f"Fehler beim Abrufen der Hardware: {e.args[0]}")

    def update_hardware_by_id(
        self,
        id:int,
        neuer_geraetetyp:str = None,
        neues_modell:str = None,
        neuer_service_tag:str = None,
        neue_ausgeliehen_von:str = None,
        neue_beschaedigung:str = None,
        neuer_standort:str = None):
        """
            Aktualisiert bestimmte Felder einer Hardware basierend auf der `ID`.

            :param int id: zum Identifizieren des Datensatzes
            :param str neuer_geraetetyp:
            :param str neues_modell:
            :param str neuer_service_tag:
            :param str neue_ausgeliehen_von: falls kein neues, leer lassen und neues Komma setzten
            :param str neue_beschaedigung: (falls kein neues, leer lassen und neues Komma setzten)
            :param str neuer_standort: (falls kein neues, leer lassen und neues Komma setzten)

        Args:
        """
        try:
            with self.__init_connection() as con:
                cur = con.cursor()
                update_fields = []
                parameters = []

                if neue_ausgeliehen_von is not None:
                    update_fields.append("Ausgeliehen_von = ?")
                    parameters.append(neue_ausgeliehen_von)
                if neuer_service_tag is not None:
                    update_fields.append("Service_Tag = ?")
                    parameters.append(neuer_service_tag)
                if neue_beschaedigung is not None:
                    update_fields.append("Beschaedigung = ?")
                    parameters.append(neue_beschaedigung)
                if neuer_standort is not None:
                    update_fields.append("Raum = ?")
                    parameters.append(neuer_standort)
                if neues_modell is not None:
                    update_fields.append("Modell = ?")
                    parameters.append(neues_modell)
                if neuer_geraetetyp is not None:
                    update_fields.append("Geraetetype = ?")
                    parameters.append(neuer_geraetetyp)
                if not update_fields:
                    return "Keine Aktualisierungsdaten vorhanden."

                sql_query = f"UPDATE Hardware SET {', '.join(update_fields)} WHERE ID = ?"
                parameters.append(id)
                self.logger.debug('sql query:'+str(sql_query))
                self.logger.debug('sql parameters:'+str(parameters))
                cur.execute(sql_query, parameters)
                con.commit()
            return "Hardware erfolgreich aktualisiert."
        except sqlite3.Error as e:
            return f"Fehler beim Aktualisieren der Hardware: {e.args[0]}"

    def execute_raw(self, command:str, expect_result = False) -> Any | None:
        with self.__init_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()
            if expect_result:
                rows = cursor.fetchall()
                return [dict(row) for row in rows]



p = PathService()
s = DbService(p)
s.execute_raw("DROP TABLE IF EXISTS Trainers")
s.execute_raw("DROP TABLE IF EXISTS Pokeoms")
s.execute_raw("CREATE TABLE IF NOT EXISTS Trainers(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(50) UNIQUE)")
s.execute_raw("CREATE TABLE IF NOT EXISTS Pokeoms(Id INTEGER PRIMARY KEY AUTOINCREMENT, Owner REFERENCES Trainer(Id), Type VARCHAR(50) UNIQUE)")
s.execute_raw("INSERT INTO Trainers (Name) VALUES ('test')")
s.execute_raw("INSERT INTO Trainers (Name) VALUES ('bla')")
print(s.execute_raw("SELECT * FROM Trainers", expect_result=True))
