from fastapi import FastAPI

# create a fastapi object
app = FastAPI()


text_posts = {1: {"title": "New Post","content": "cool test post"}}


# create an endpoint for text posts
@app.get("/posts")
def get_all_posts():
    return text_posts

 
# create an endpoint with a path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    return text_posts.get(id)