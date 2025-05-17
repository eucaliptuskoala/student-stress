from abc import ABC, abstractmethod

class IPreprocessing(ABC):
    @abstractmethod
    def rename(self):
        pass

    @abstractmethod
    def convert_to_numeric(self):
        pass

    @abstractmethod
    def drop_columns(self):
        pass