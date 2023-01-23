from typing import Union
from fastapi import FastAPI, File, UploadFile
import json
from models.comment import CommentWebHook
from pydantic import BaseModel


app = FastAPI()


class Test():
    id: int
    user_id: int
    text: str


print("Started")


#@app.get("/test")
#def test(test : Test):
#    return test

class someItem(BaseModel):
    name: str
    price: float

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    nn: someItem
    tags: list[str] = []


@app.post("/CommentWebHook/")
async def NewCommentWebHook(CommentWebHookInfo: CommentWebHook) -> CommentWebHook:
    print(CommentWebHookInfo.user)
    return CommentWebHookInfo

@app.post("/items/")
async def create_item(item: Item):
    return item

#@app.get("/items/")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

@app.post("/issue.json")
def create_upload_files(upload_file: UploadFile = File(...)):
    f = open("input.txt", mode='w+')
    f.write(upload_file.File.read())
    f.close()

