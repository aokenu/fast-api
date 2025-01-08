from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from app.schemas import PostCreate, PostResponse


# connection string for postgresql: postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Production_DB")

# create a fastapi object
app = FastAPI()


text_posts = {
 1: {'title': 'Random Thought', 'content': 'deploying new features'},
 2: {'title': 'Random Thought', 'content': 'fixing bugs in production'},
 3: {'title': 'Engineering Notes', 'content': 'testing API endpoints'},
 4: {'title': 'Data Life', 'content': 'writing clean Python code'},
 5: {'title': 'Pipeline Diary', 'content': 'working on data pipelines'},
 6: {'title': 'Debug Session', 'content': 'writing clean Python code'},
 7: {'title': 'Data Life', 'content': 'monitoring system performance'},
 8: {'title': 'Data Life', 'content': 'cool test post'},
 9: {'title': 'System Update', 'content': 'ETL job completed successfully'},
 10: {'title': 'New Post', 'content': 'writing clean Python code'}
}


# create an endpoint for text posts
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


# a get endpoint that return sql query result from postgresql
@app.get("/get_query")
def get_sql_query():
    with engine.connect() as conn:
        sql_query = conn.execute(text('SELECT * FROM "DimCustomer"'))
        return sql_query.mappings().all()

 
# create an endpoint with a path parameter
@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)



# create a post endpoint
@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
