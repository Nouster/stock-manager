from abc import ABC, abstractmethod

class AbstractDatabaseConnection(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass
