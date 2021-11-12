from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

@app.get("/")
async def root():
    return {"message":"Hello World!"}
#min 47:35

@app.get("/posts")
async def get_posts():
    return {"data":"this is a post"}

"""
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
"""

"""
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.rating)
    return {"posty": "new post"}
"""

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"posty": new_post.dict()}