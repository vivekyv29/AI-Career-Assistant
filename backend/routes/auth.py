from fastapi import APIRouter
from fastapi import Depends

from pydantic import BaseModel

from sqlalchemy.orm import Session

from database.dependency import get_db

from models.user import User

from utils.security import hash_password
from utils.security import verify_password
from utils.jwt_handler import create_access_token
router = APIRouter()

class LoginRequest(BaseModel):

    email: str

    password: str
class RegisterRequest(BaseModel):

    name: str

    email: str

    password: str


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:

        return {
            "message":
            "Email already exists"
        }

    user = User(

        name=request.name,

        email=request.email,

        password=hash_password(
            request.password
        )
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {

        "message":
        "User Registered Successfully",

        "user_id":
        user.id
    }

@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:

        return {
            "message":
            "Invalid Email"
        }

    if not verify_password(
        request.password,
        user.password
    ):

        return {
            "message":
            "Invalid Password"
        }

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "access_token": token
    }