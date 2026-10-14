import bcrypt # 这个是专门存储密码设计的哈希算法


def hash_password(password: str) -> str:
    """对密码进行加密"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashend_password: str):
    """验证密码的有效性"""
    """ "123" -> "xxxsdada" """
    return bcrypt.checkpw(password.encode("utf-8"), hashend_password.encode("utf-8"))
