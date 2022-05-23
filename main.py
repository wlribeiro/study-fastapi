from fastapi import FastAPI
from todo import router as todo_router

app  = FastAPI()



@app.get("/")
def hello_world():
    """
    Root view, returns {"hello": "world"}
    """
    return {"hello":"world"}


app.include_router(todo_router, prefix="/to-do")
