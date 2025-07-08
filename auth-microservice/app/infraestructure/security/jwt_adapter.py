from app.domain.ports.output.jwt_generator_port import JwtGenerator
from app.domain.ports.output.jwt_validator_port import JwtValidatorPort
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt

from app.domain.ports.output.workshop_repository_port import WorkShopRepositoryPort


SECRET_KEY = "SaaS-tallerweb"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 5

class SimpleJwtGenerator(JwtGenerator):
    def generate(self, subject: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES)
        payload = {
            "sub": subject, 
            "exp": expire
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


class JwtValidatorPortImpl(JwtValidatorPort):

    def validate(self, token: str) -> Optional[str]:
        """
        Solo valida la estructura y expiración del token JWT
        Retorna el email del usuario si el token es válido
        """
        try:
            # 1. Decodificar el token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            
            # 2. Verificar que el token no haya expirado
            exp = payload.get("exp")
            if exp is None:
                return None
                
            current_time = datetime.now(timezone.utc).timestamp()
            if current_time > exp:
                return None
            
            # 3. Obtener el email del token
            workshop_email = payload.get("sub")
            if not workshop_email:
                return None
            
            # 4. Retornar el email (la validación contra BD se hace en el caso de uso)
            return workshop_email
            
        except JWTError:
            return None
        except Exception:
            return None
