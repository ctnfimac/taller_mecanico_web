from fastapi import APIRouter, HTTPException, Depends
#from fastapi import FastAPI, HTTPException, Depends
#from fastapi.security import OAuth2PasswordRequestForm
#from schemas import LoginRequest, TokenResponse
from app.infraestructure.schemas.auth import LoginResponse, LoginRequest
#from auth import verify_password, create_access_token
#from models import fake_user_db
from datetime import timedelta
#from application.services.auth_service import AuthService
from sqlalchemy.orm import Session
from app.infraestructure.repository.conection_db import get_db
from app.infraestructure.security.jwt_adapter import SimpleJwtGenerator
from app.application.usecases.login_usecase_impl import LoginUseCaseImpl
from app.infraestructure.repository.workshop_repository_impl import WorkShopRepositoryImpl

router_auth_api = APIRouter()


@router_auth_api.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    usecase = LoginUseCaseImpl(
        workshop_repo=WorkShopRepositoryImpl(db),
        jwt_gen=SimpleJwtGenerator()
    )
    try:
        token = usecase.login(data.email, data.password)
        return LoginResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))