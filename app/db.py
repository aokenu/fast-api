from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime



# connection string for postgresql: postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
DATABASE_URL = "postgresql+psycopg://postgres:root@localhost:5432/Production_DB"


# Base class for all SQLAlchemy ORM models
# DeclarativeBase provides metadata and mapping functionality
class Base(DeclarativeBase):
    # No fields here; this class exists to be inherited by all models
    pass


# ORM model representing the "posts" table
class Post(Base):
    # Explicitly set the table name in the database
    __tablename__ = "posts"

    # Primary key column
    # Uses UUID instead of integer IDs
    # uuid.uuid4 is called automatically when a new Post is created
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Optional text caption for the post
    caption = Column(Text)

    # URL pointing to where the uploaded file is stored
    # Cannot be NULL in the database
    url = Column(String, nullable=False)

    # Type of file (e.g., photo, video)
    # Required field
    file_type = Column(String, nullable=False)

    # Original name of the uploaded file
    # Required field
    file_name = Column(String, nullable=False)

    # Timestamp for when the record was created
    # Defaults to the current UTC time when inserted
    created_at = Column(DateTime, default=datetime.utcnow)



# Create an asynchronous SQLAlchemy engine
# This manages the database connection pool
engine = create_async_engine(DATABASE_URL)

# Factory for creating AsyncSession objects
# expire_on_commit=False prevents objects from being invalidated after commit
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False
)


# Creates database tables based on all models that inherit from Base
# Intended to run once during application startup
async def create_db_and_tables(): 
    # Begin an async database connection context
    async with engine.begin() as conn: 
        # Run the synchronous create_all method in an async-safe way
        # This creates tables if they do not already exist
        await conn.run_sync(Base.metadata.create_all) 


# Dependency function that provides an async database session
# Used with FastAPI's Depends()
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    # Create a new AsyncSession
    async with async_session_maker() as session:
        # Yield the session to the request handler
        # FastAPI ensures this session is properly closed after use
        yield session
