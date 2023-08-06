# coding: utf-8
# Copyright (c) OMG-WRITER (2023)
# Author: TianD (huiguoyu)
import secrets

from fastapi import HTTPException, APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Any

from sqlalchemy.orm import Session

from data.database import get_db
from domain.models import User
from data.schemas import UserIn, UserOut


# 加密相关配置
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = secrets.token_urlsafe(32)
SECRET_KEY = '1UwQhcS_sPL1uBtTng7fzKaKi3mcAvJaG25jJTGLJrg'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 路由路径常量
PREFIX = "/auth"
TAGS = ["auth"]
REGISTER_PATH = "/register"
LOGIN_PATH = "/login"
LOGOUT_PATH = "/logout"

router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= PREFIX + LOGIN_PATH)


# 生成访问令牌
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 验证密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# 创建哈希密码
def get_password_hash(password):
    return pwd_context.hash(password)


# 获取当前用户
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# 注册用户
@router.post(REGISTER_PATH, response_model=UserOut)
def register(user: UserIn, db: Session = Depends(get_db)) -> Any:
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user_obj = User(**user.dict())
    user_obj.password = get_password_hash(user.password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


# 用户登录
@router.post(LOGIN_PATH, response_model=None)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


# 用户登出
@router.post(LOGOUT_PATH)
def logout():
    return {"message": "User logged out successfully"}


@router.get("/protected")
def protected_route(user: User = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")
    # 执行受保护的操作
    return {"message": "Protected route accessed by authorized user"}