
from abc import ABC, abstractmethod

class IProduct(ABC):
    
    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def add_product(self, name, reference, quantity):
        pass

    @abstractmethod
    def close_connection(self):
        pass