from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from app.schemas import PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


# create a fastapi object
app = FastAPI(lifespan=lifespan)

