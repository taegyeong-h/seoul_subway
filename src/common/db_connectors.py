import polars from pl
from abc import ABC, abstractmethod



class BaseDBConnector(ABC):
    @abstractmethod
    def get_connection_url(self) -> str:
