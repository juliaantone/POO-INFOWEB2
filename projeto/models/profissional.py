from models.profissional import Profissional
import json

class ProfissionalDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()