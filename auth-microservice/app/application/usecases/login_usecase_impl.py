from app.domain.ports.input.auth_usecase import AuthUseCase
from app.domain.ports.output.workshop_repository_port import WorkShopRepositoryPort
from app.domain.ports.output.jwt_generator_port import JwtGenerator
from app.application.services.auth_service import verify_password

class LoginUseCaseImpl(AuthUseCase):
    
    def __init__(self, workshop_repo: WorkShopRepositoryPort, jwt_gen: JwtGenerator):
        self.workshop_repo = workshop_repo
        self.jwt_gen = jwt_gen
    

    def login(self, email: str, password: str) -> str:
        user = self.workshop_repo.find_by_email(email)
        if not user or not verify_password(password, user.password):
            raise Exception("Invalid credentials")
        return self.jwt_gen.generate(str(user.id))