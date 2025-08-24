from abc import ABC, abstractmethod
from app.schemas.tags.tags_schema import TagSchema

class TagEntities(ABC):
    
    @abstractmethod
    def incluir_tag(self, cadastro: TagSchema): pass
    
    @abstractmethod
    def listar_tag(self): pass
