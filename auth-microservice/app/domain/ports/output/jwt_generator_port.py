from abc import ABC, abstractmethod

class JwtGenerator(ABC):
    
    @abstractmethod
    def generate(self, subject: str, workshop_id: int) -> str:
        pass