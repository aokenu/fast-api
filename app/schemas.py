from pydantic import BaseModel


# Create a class
class PostResponse(BaseModel):
    title: str
    content: str