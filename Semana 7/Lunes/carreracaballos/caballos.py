from mailbox import NoSuchMailboxError
from turtle import color


class Caballo:
    def __init__(self,nombre,color,edad) -> None:
        self.nombre=nombre
        self.color=color
        self.edad=edad