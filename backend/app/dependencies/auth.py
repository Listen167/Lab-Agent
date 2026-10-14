from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.dataset import get_db
from app.utils.jwt import decode_access_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """JWT token 鉴权验证合法性（验证前端传过来的是否具有合法性）"""
    try:
        # 1. 解析Token (decode_access_token 内部已经捕获异常，失败会返回() )
        payload = decode_access_token(token)  # 负载

    # 2. 如果解析结果为空自带你，说明Token过期或者无效
    except Exception:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="登录已失效，请重新登录"
        )
    # 3. 获取用户id
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的登录凭证"
        )

    # 4. 从数据库根据用户 ID 查询用户信息
    user = db.query(User).filter(User.id == user_id).first()

    # 5. 判断用户是否存在（重要！防止用户被删了 Token 还在）
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="用户不存在或已被删除"
        )
    
    # 6. 判断用户是否被禁用（status != 1）
    if user.status != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="用户被禁用"
        )
    
    return user
