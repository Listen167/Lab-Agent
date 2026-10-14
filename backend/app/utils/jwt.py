import jwt
from datetime import datetime, timedelta

from app.config import settings


def create_access_token(user_id: int) ->str:
    """创建JWT token"""
    # 计算过期时间
    expire = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)

    payload = {"user_id": user_id, "exp": expire}

    # algorithm是使用签名算法
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    """解析JWT token"""
    # 解析的时候algorithms必须是列表！
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # token已过期
        return {}
    except jwt.InvalidTokenError:
        # token 无效（被篡改和伪造等）
        return {}