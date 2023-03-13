# emulando o conceito de interfaces 
from abc import ABC, abstractclassmethod

# ? Classes abstratas impossibilita a instancia porque 
# ? essa classe vai entrar como herança
class database(ABC):
    @abstractclassmethod
    def insert():
        raise Exception("Should implement method: insert")

    @abstractclassmethod
    def select():
        pass