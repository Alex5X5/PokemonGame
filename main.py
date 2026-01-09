import sys
import socket
from queue import Queue
from ipaddress import ip_address
from threading import Thread
from subprocess import check_output
from tkinter.ttk import (
    Label, Entry,
)
from tkinter import (
    Tk, Button, Text, StringVar, END,
    Toplevel, BOTH
)

import PokemonApp


# from tkinter.messagebox import showinfo
# we need to make our own showinfo widget


def validate_ip(ip):
    """
    Validate an ip address
    if the address is a valid ipv4 or ipv6 address
    the functions returns True, otherwise
    it returns False

    """
    try:
        ip_address(ip)
    except:
        return False
    else:
        return True


class Showinfo(Toplevel):
    """
    Spawns a new Toplevel window.
    """

    def __init__(self, *, title, msg, width, height):
        super().__init__(width=width, height=height)
        self.title(title)
        Label(self, text=msg).pack(fill=BOTH)
        Button(self, text="Ok", command=self.destroy).pack(fill=BOTH)


"""
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('My Ping GUI')
        # self.geometry('500x400')
        self.ping_active = False
        self.validation_queue = Queue()
        self.validation_loop()
        self.ip = StringVar(self)
        self.ip.trace_add("write", self.validate)
        self.setup()

    def setup(self):
        Label(self, text="Enter target IP or host as required.").pack()
        Entry(self, textvariable=self.ip).pack()
        ping_button = Button(self, text="Ping Test", command=self.ping)
        ping_button.pack()
        self.ping_button = ping_button
        self.textbox = Text(self, width=150, height=10)
        self.textbox.pack(fill=BOTH)
        Button(self, text="Exit", command=self.destroy).pack()

    def validate(self, *args):
        self.validation_queue.put(self.ip.get())

    def validation_loop(self):
        self._validation_loop = Thread(target=self._validation_worker, daemon=True)
        self._validation_loop.start()

    def set_ping_color(self, color):
        self.ping_button['activebackground'] = color
        self.ping_button['bg'] = color
        self.ping_button['highlightbackground'] = color

    def _validation_worker(self):
        while True:
            ip_or_host = self.validation_queue.get()
            is_ip = validate_ip(ip_or_host)
            if is_ip:
                self.set_ping_color("green")
            else:
                self.set_ping_color("red")
            # is useful if you want to join a queu
            # then join blocks, until all tasks are done
            self.validation_queue.task_done()

    def ping(self):
        if not self.ping_active:
            self.ping_active = True
            self.textbox.delete(1.0, END)
            ip = self.ip.get()
            thread = Thread(target=self.ping_thread)
            thread.start()

    def ping_thread(self):
        # code tested on linux
        # ping on windows has different options
        stdout = check_output(['ping', self.ip.get()], encoding="ansi")
        # print(stdout)
        self.textbox.insert(END, stdout)
        Showinfo(title='Results', msg=stdout, width=500, height=100)
        self.ping_active = False


App().mainloop()"""

PokemonApp.PokemonApp()
