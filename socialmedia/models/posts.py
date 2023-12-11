from pydantic import BaseModel


class UserPostIn(BaseModel):
    post: str

class UserPost(UserPostIn):
    id: int