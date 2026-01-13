import sqlite3
from typing import Any, Type, Final

from Logic.Models.Pokemons.Arkani import Arkani
from Logic.Models.Pokemons.Pokemon import Pokemon
from Logic.Models.Trainer import Trainer
from Logic.Services.LoggingService import Logger
from Logic.Services.PathService import PathService
from Logic.Services.RegsitryService import RegistryService


class DbService:

    POKEMON_TYPE_KEY:Final[str] = 'Type'
    POKEMON_EXPERIENCE_KEY:Final[str] = 'Experience'
    POKEMON_OWNER_KEY:Final[str] = 'TrainerId'

    TRAINER_NAME_KEY:Final[str] = 'Name'


    def __init__(self, path_service: PathService, registry_service:RegistryService):
        self.__path_service: PathService = path_service
        self.__registry_service:RegistryService = registry_service
        self.logger: Logger = Logger('DbService')
        self.__chain_execution_connection: sqlite3.Connection | None = None

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

    def load_trainer(self, trainer_name: str) -> Trainer:
        trainer_data: list[dict[str, Any]] = self.execute_raw(f"SELECT * FROM Trainers WHERE Name=\"{trainer_name}\"", expect_result=True)
        trainer: Trainer = Trainer.from_dictionary(trainer_data[0])
        pokemon_data: list[dict[str, Any]] = self.execute_raw(f"SELECT * FROM Pokemons WHERE TrainerId=\"{trainer.Id}\"", expect_result=True)
        for data in pokemon_data:
            pokemon_type:Type = self.__registry_service.find_pokemon_type([data["Type"]])
            if pokemon_type is not None:
                pokemon:Pokemon = pokemon_type(trainer)
                trainer.pokemons.append(pokemon)
        return trainer

    def insert_or_update_trainer(self, trainer: Trainer):
        self.execute_raw(f"INSERT OR IGNORE INTO Trainers (Name, Id) VALUES ('{trainer.Name}', {trainer.Id})")
        self.execute_raw(f"UPDATE Trainers SET Name='{trainer.Name}' WHERE Id={trainer.Id}")

    def execute_raw(self, command: str, expect_result=False) -> Any | None:
        with self.__init_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()
            if expect_result:
                rows = cursor.fetchall()
                return [dict(row) for row in rows]

    def start_chain_execution(self) -> 'DbService':
        self.__chain_execution_connection = self.__init_connection()
        return self

    def execute_raw_chained(self, command: str, refenece: dict[str, Any] | None = None, expect_result=False) -> 'DbService':
        if self.__chain_execution_connection is not None:
            cursor = self.__chain_execution_connection.cursor()
            cursor.execute(command)
            self.__chain_execution_connection.commit()
            if expect_result:
                rows = cursor.fetchall()
                refenece = [dict(row) for row in rows]
        return self

    def finish_chain_execution(self) -> 'DbService':
        if self.__chain_execution_connection is not None:
            self.__chain_execution_connection.close()
        return self


p = PathService()
r = RegistryService()
s = DbService(p, r)
s.start_chain_execution()\
    .execute_raw_chained(f"DROP TABLE IF EXISTS Trainers")\
    .execute_raw_chained(f"DROP TABLE IF EXISTS Pokemons")\
    .execute_raw_chained(f"CREATE TABLE IF NOT EXISTS Trainers(Id INTEGER PRIMARY KEY AUTOINCREMENT, {DbService.TRAINER_NAME_KEY} VARCHAR(50) UNIQUE)")\
    .execute_raw_chained(f"CREATE TABLE IF NOT EXISTS Pokemons(Id INTEGER PRIMARY KEY AUTOINCREMENT, {DbService.POKEMON_TYPE_KEY} VARCHAR(50) UNIQUE, {DbService.POKEMON_EXPERIENCE_KEY} REAL, {DbService.POKEMON_OWNER_KEY} INTEGER NOT NULL, FOREIGN KEY (TrainerId) REFERENCES Trainers (Id))")\
    .execute_raw_chained(f"INSERT INTO Trainers (Name) VALUES ('test')")\
    .execute_raw_chained(f"INSERT INTO Trainers (Name) VALUES ('bla')")\
    .finish_chain_execution()
test_trainer:Trainer = s.load_trainer("test")
s.execute_raw(f"INSERT INTO Pokemons({DbService.POKEMON_TYPE_KEY}, {DbService.POKEMON_EXPERIENCE_KEY}, {DbService.POKEMON_OWNER_KEY}) VALUES ('{Arkani.__name__}', 3599.4, {test_trainer.Id})")
print(s.execute_raw(f"SELECT * FROM Pokemons WHERE TrainerId={test_trainer.Id}", expect_result=True))