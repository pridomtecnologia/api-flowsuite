from abc import ABC, abstractmethod

class UsuarioEntidade(ABC):
    
    @abstractmethod
    def user_register(self, user): pass

    def list_users(self): pass
    
    def update_user(self, id_user, user): pass
    
    def delete_user(self, id_user): pass

    @abstractmethod
    def user_login(self, user, expires_in): pass