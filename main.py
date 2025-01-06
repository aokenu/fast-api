import uvicorn
from app.app import app
from sqlalchemy import create_engine, text
from tabulate import tabulate


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)