class Instrutor:
    def __init__(self, id_instrutor: int, nome: str, especialidade: str):
        self.__id_instrutor = id_instrutor
        self.__nome = nome
        self.__especialidade = especialidade

    # --- Getters ---
    def get_id_instrutor(self) -> int:
        return self.__id_instrutor

    def get_nome(self) -> str:
        return self.__nome

    def get_especialidade(self) -> str:
        return self.__especialidade

    # --- Setters ---
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_especialidade(self, especialidade: str):
        self.__especialidade = especialidade

    # --- Método to_string --- [cite: 156]
    def to_string(self) -> str:
        return f"ID: {self.get_id_instrutor()} | Nome: {self.get_nome()} | Especialidade: {self.get_especialidade()}"