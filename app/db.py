from collections.abc import AsyncGenerator
import uuid


from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationship


# connection string for postgresql: postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/Production_DB"



class Post(DeclarativeBase):
    __table__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    

