
from abc import ABC, abstractmethod

class ITableOperation(ABC):
    
    @abstractmethod
    def get_all_entries(self):
        pass

    @abstractmethod
    def add_entry(self, name, reference, quantity):
        pass

    @abstractmethod
    def close_connection(self):
        pass