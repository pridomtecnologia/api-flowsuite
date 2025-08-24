from abc import ABC, abstractmethod
from app.schemas.cadastros.cadastro_schemas import RegisterSchema

class CadastroEntities(ABC):
    
    @abstractmethod
    def incluir_cadastro(self, cadastro: RegisterSchema): pass
    
    @abstractmethod
    def listar_cadastro(self): pass

    @abstractmethod
    def atualizar_cadastro(self, id_cadastro: int, cadastro): pass
    
    @abstractmethod
    def deletar_cadastro(self, id_cadastro: int): pass