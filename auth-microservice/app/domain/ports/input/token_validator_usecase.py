from abc import ABC, abstractmethod
from typing import Optional



class TokenValidatorUseCase(ABC):
    @abstractmethod
    def validate(self, token: str) -> Optional[str]:
        """
        Valida un token JWT y retorna el subject (workshop) si es válido
        Retorna None si el token es inválido
        """
        pass