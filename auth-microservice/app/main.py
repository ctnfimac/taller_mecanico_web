from fastapi import FastAPI #, HTTPException, Depends
from app.infraestructure.api.v1.auth_controller import router_auth_api
# from fastapi.security import OAuth2PasswordRequestForm
# from schemas import LoginRequest, TokenResponse
# from auth import verify_password, create_access_token
# from models import fake_user_db
# from datetime import timedelta



app = FastAPI()

app.include_router(router_auth_api)