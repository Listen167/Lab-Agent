from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    """
    返回用户信息给前端，
    数据来自ORM，需要from_attributes转换
    """
    id: int
    username: str
    name: str
    role: str
    email: str | None = None
    phone: str | None = None
    status: int

    model_config = ConfigDict(from_attributes=True)