from abc import ABC, abstractmethod
from typing import Optional


class JwtValidatorPort(ABC):
    @abstractmethod
    def validate(self, token: str) -> Optional[str]:
        """
        Valida un token JWT y retorna el subject si es válido
        """
        pass