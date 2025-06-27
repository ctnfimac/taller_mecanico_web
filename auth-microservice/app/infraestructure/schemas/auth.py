from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="El correo electrónico es obligatorio.")
    password: str = Field(..., description="La contraseña es obligatoria.")

class LoginResponse(BaseModel):
    access_token: str  
    token_type: str = "bearer"
