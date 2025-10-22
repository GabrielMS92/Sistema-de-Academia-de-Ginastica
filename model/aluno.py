from model.instrutor import Instrutor

class Aluno:
    def __init__(self, id_aluno: int, nome: str, email: str, instrutor: Instrutor = None):
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__email = email
        self.__instrutor = instrutor # Armazena o objeto Instrutor [cite: 153]

    # --- Getters ---
    def get_id_aluno(self) -> int:
        return self.__id_aluno

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_instrutor(self) -> Instrutor:
        return self.__instrutor

    # --- Setters ---
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_email(self, email: str):
        self.__email = email
        
    def set_instrutor(self, instrutor: Instrutor):
        self.__instrutor = instrutor

    # --- Método to_string ---
    def to_string(self) -> str:
        instrutor_nome = "Sem instrutor"
        if self.get_instrutor():
            instrutor_nome = self.get_instrutor().get_nome()
            
        return f"ID: {self.get_id_aluno()} | Nome: {self.get_nome()} | Email: {self.get_email()} | Instrutor: {instrutor_nome}"
