from pydantic import BaseModel

class LoginRequest(BaseModel):
    """
    要是想要调用登录接口，请求体(body)，
    一定要包含下面两个字符串子字段
    接收前登录数据，数据来最JSON，不需要from_attributes
    """
    username: str
    password: str