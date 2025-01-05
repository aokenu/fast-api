from fastapi import FastAPI, HTTPException

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
    return text_posts

 
# create an endpoint with a path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)