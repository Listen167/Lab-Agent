from fastapi import APIRouter, Depends
from app.common.response import Response
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.dataset import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token

# 给这个router下所有接统一加上/api/auth前缀
router = APIRouter(prefix="/auth", tags=["权限验证"])


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # 先注入数据库会话
    # 查找数据库， 返回User的ORM对象或者None
    user = db.query(User).filter(User.username == data.username).first()

    # 判断账号和密码是否正确(校验)
    if not user or not verify_password(data.password, user.password):
        return Response.error(message="账号或密码错误")
    # 验证账号的状态
    if user.status != 1:
        return Response.error(message= "账号已被禁用")

    # 创建token
    token = create_access_token(user.id)

    # 返回信息
    return Response.success(
        data={"token": token, "user": UserResponse.model_validate(user)}
    )
