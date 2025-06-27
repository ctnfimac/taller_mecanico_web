from app.domain.ports.output.jwt_generator_port import JwtGenerator
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "una_clave_super_segura"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 1

class SimpleJwtGenerator(JwtGenerator):
    def generate(self, subject: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES)
        payload = {"sub": subject, "exp": expire}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
