from abc import ABC, abstractmethod

class UsuarioEntidade(ABC):
    
    @abstractmethod
    def user_register(self, user): pass
    
    @abstractmethod
    def user_login(self, user, expires_in): pass