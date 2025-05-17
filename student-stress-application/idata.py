from abc import ABC, abstractmethod
import pandas as pd

class IData(ABC):
    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        pass