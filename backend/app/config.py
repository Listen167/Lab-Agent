from pydantic_settings import BaseSettings, SettingsConfigDict # BaseSetings是让配置类自己去.env去找配置，而SettingsConfig是告诉BaseSettings去那里找
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # 后端项目的根路径
ENV_FILE = BASE_DIR / ".ENV"


class Settings(BaseSettings):
    DATABASE_URL: str 
    JWT_SECRET_KEY: str
    JWT_EXPIRE_HOURS: int = 24
    JWT_ALGORITHM:str = "HS256"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, 
        env_file_encoding="utf-8"
    )

settings = Settings()