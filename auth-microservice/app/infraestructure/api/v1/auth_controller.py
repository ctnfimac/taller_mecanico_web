from fastapi import APIRouter, HTTPException, Depends, status
from app.application.usecases.token_validator_usecase_impl import TokenValidatorUseCaseImpl
from app.infraestructure.schemas.auth import LoginResponse, LoginRequest, TokenValidationRequest, TokenValidationResponse
from sqlalchemy.orm import Session
from app.infraestructure.repository.conection_db import get_db
from app.infraestructure.security.bcrypt_password_hasher import BcryptPasswordHasher
from app.infraestructure.security.jwt_adapter import JwtValidatorPortImpl, SimpleJwtGenerator
from app.application.usecases.login_usecase_impl import LoginUseCaseImpl
from app.infraestructure.repository.workshop_repository_impl import WorkShopRepositoryImpl

router_auth_api = APIRouter()


@router_auth_api.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    usecase = LoginUseCaseImpl(
        workshop_repo=WorkShopRepositoryImpl(db),
        jwt_gen=SimpleJwtGenerator(),
        password_hasher=BcryptPasswordHasher()
    )
    try:
        token = usecase.login(data.email, data.password)
        return LoginResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    

@router_auth_api.post("/validate-token", response_model=TokenValidationResponse, status_code=status.HTTP_200_OK)
def validate_token(request: TokenValidationRequest,  db: Session = Depends(get_db)):
    # Inyección de dependencias
    workshop_repo = WorkShopRepositoryImpl(db)
    jwt_validator = JwtValidatorPortImpl()  
    use_case = TokenValidatorUseCaseImpl(jwt_validator, workshop_repo)
    
    # Validar el token (incluye validación contra BD)
    workshop_email = use_case.validate(request.token)
    
    if workshop_email:
        return TokenValidationResponse(
            valid=True,
            email=workshop_email,
            message="Token válido"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido, expirado o usuario no encontrado"
        )