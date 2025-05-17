from abc import ABC, abstractmethod

class IModel(ABC):
    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def predict(self, new_data):
        pass