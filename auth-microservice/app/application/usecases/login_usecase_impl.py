from app.domain.ports.input.auth_usecase import AuthUseCase
from app.domain.ports.output.password_hasher import PasswordHasher
from app.domain.ports.output.workshop_repository_port import WorkShopRepositoryPort
from app.domain.ports.output.jwt_generator_port import JwtGenerator

class LoginUseCaseImpl(AuthUseCase):
    
    def __init__(
        self,
        workshop_repo: WorkShopRepositoryPort,
        jwt_gen: JwtGenerator,
        password_hasher: PasswordHasher
    ):
        self.workshop_repo = workshop_repo
        self.jwt_gen = jwt_gen
        self.password_hasher = password_hasher
    

    def login(self, email: str, password: str) -> str:
        user = self.workshop_repo.find_by_email(email)
        # if not user or not verify_password(password, user.password):
        if not user or not self.password_hasher.verify(password, user.password):
            #TODO crear excepcion personalizada
            raise Exception("Invalid credentials")
        return self.jwt_gen.generate(user.email, user.id)