from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: str
