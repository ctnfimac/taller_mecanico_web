from pydantic import BaseModel, EmailStr, Field

# PARA EL INICIO DE SESIÓN
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="El correo electrónico es obligatorio.")
    password: str = Field(..., description="La contraseña es obligatoria.")

class LoginResponse(BaseModel):
    access_token: str  
    token_type: str = "bearer"


# PARA LA VALIDACION DEL TOKEN
class TokenValidationRequest(BaseModel):
    token: str

class TokenValidationResponse(BaseModel):
    valid: bool
    email: str = None
    message: str = None