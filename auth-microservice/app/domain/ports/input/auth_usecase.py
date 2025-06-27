from abc import abstractmethod
from abc import ABC

class AuthUseCase(ABC):
    
    @abstractmethod
    def login(self, email:str, password:str) -> str:
        pass