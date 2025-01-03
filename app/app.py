from fastapi import FastAPI

# create a fastapi object
app = FastAPI()


# create an endpoint
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}