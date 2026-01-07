from passlib.context import CryptContext
from app.domain.ports.output.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def verify(self, plain: str, hashed: str) -> bool:
        return self.pwd_context.verify(plain, hashed)