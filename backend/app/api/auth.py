from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.dataset import get_db
from app.models.user import User
from app.schemas.user import UserResponse

# 给这个router下所有接统一加上/api/auth前缀
router= APIRouter(prefix="/api/auth", tags=["权限验证"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # 先注入数据库会话
    # 查找数据库， 返回User的ORM对象或者None
    user = db.query(User).filter(User.username == data.username).first()

    # 判断账号和密码是否正确(校验)
    if not user or user.password != data.password:
        return { "code": 400, "message": "账号或者密码错误"}
    return{
        "code":200,
        "message": "操作成功",
        "data": UserResponse.model_validate(user)
    }
  
