from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, DateTime
from app.config import settings
from datetime import datetime

# 1. 创建引擎
engine = create_engine(settings.DATABASE_URL)

# 2. 创建会话工厂（建议补上 autocommit=False）
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 3. 依赖注入函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: # 请求结束就会自动关闭
        db.close()

# 4. 定义所有模型的基础类
class Base(DeclarativeBase):
    # 主键：自增、整数类型
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment="主键ID") # 唯一身份证（id）, 设置自增
    
    # 创建时间：插入时自动填充当前时间
    create_time: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now, 
        comment="创建时间"
    )
    
    # 更新时间：插入时填充当前时间，且每次更新数据时自动刷新
    update_time: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now, 
        onupdate=datetime.now,  
        comment="更新时间"
    )