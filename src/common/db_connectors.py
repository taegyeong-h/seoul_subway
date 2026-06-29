
from abc import ABC, abstractmethod



class BaseDBConnector(ABC):
    @abstractmethod
    def get_connection_url(self) -> str:
        pass


class PostgresDBConnector(BaseDBConnector):
    def __init__(self, db_config: dict):
        self.user = db_config["user"]
        self.password = db_config["password"]
        self.host = db_config["host"]
        self.port = db_config["port"]
        self.database_name = db_config["database_name"]

    def get_connection_url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}"