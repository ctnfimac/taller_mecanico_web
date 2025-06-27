from abc import ABC, abstractmethod

class JwtGenerator(ABC):
    
    @abstractmethod
    def generate(self, subject: str) -> str:
        pass