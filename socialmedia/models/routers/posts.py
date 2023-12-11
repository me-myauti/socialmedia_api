from fastapi import APIRouter
from socialmedia.models.posts import UserPost, UserPostIn

router = APIRouter()

post_table = {}

@router.post("/post", response_model=UserPost)
async def create_post(data: UserPostIn):
    res = data.model_dump()
    last_record_id = len(post_table)
    new_post = {**res, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post

@router.get("/post", response_model=list[UserPost])
async def get_post():
    return list(post_table.values())