from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime



# connection string for postgresql: postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
DATABASE_URL = "postgresql+psycopg://postgres:root@localhost:5432/Production_DB"


