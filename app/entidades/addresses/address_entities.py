from abc import ABC, abstractmethod

class AddressEntities(ABC):
    
    @abstractmethod
    def create_address(self, address, owner_type, owner_id): pass