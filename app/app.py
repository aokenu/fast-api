from fastapi import FastAPI

# create a fastapi object
app = FastAPI()


text_posts = []


# create an endpoint for text posts
@app.get("/posts")
def get_all_posts():
    return text_posts