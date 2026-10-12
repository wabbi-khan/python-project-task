from sqlalchemy import Column, Integer, String, Boolean
from src.utils.db import Base

class TashModel(Base):
    __tablename__= "user_tasks"

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String,index=True)
    description=Column(String)
    is_completed=Column(Boolean,default=False)
    # created_at=Column(DateTime,default=func.now())
    # updated_at=Column(DateTime,default=func.now(),onupdate=func.now())
    
