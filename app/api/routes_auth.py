from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(auth_input: AuthInput):
    # Dummy authentication logic
    if auth_input.username == "admin" and auth_input.password == "password":
        token = create_token(data={"sub": auth_input.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        return {"error": "Invalid credentials"}