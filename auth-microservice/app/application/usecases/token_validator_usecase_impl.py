from app.domain.ports.output.jwt_validator_port import JwtValidatorPort
from app.domain.ports.input.token_validator_usecase import TokenValidatorUseCase
from app.domain.ports.output.workshop_repository_port import WorkShopRepositoryPort
from typing import Optional


class TokenValidatorUseCaseImpl(TokenValidatorUseCase):
    def __init__(self, jwt_validator: JwtValidatorPort, workshop_repo: WorkShopRepositoryPort):
        self.jwt_validator = jwt_validator
        self.workshop_repo = workshop_repo
    
    def validate(self, token: str) -> Optional[str]:
        # 1. Validar formato y expiración del token
        workshop_email = self.jwt_validator.validate(token)
        
        if not workshop_email:
            return None
        
        # 2. Verificar que el usuario existe en la base de datos
        workshop = self.workshop_repo.find_by_email(workshop_email)
        if not workshop:
            return None
        
        return workshop_email
