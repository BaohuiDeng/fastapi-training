from fastapi import APIRouter
from fastapi_training.Handlers.oauth2 import get_current_user
from fastapi_training.model.blog import Blog
from fastapi_training.Handlers import blog_handler
from fastapi_training.model.user_model import User
from fastapi import Depends


router = APIRouter(
    prefix="/blog",
    tags=['Blog'])

@router.get("/")
def get_blogs(get_current_user: User = Depends(get_current_user)):
    return blog_handler.get_all_blogs()



@router.get("/{id}")
def get_blog(id: int,get_current_user: User = Depends(get_current_user)):
  return blog_handler.get_blog_by_id(id)


@router.post("/")
def create_blog(blog: Blog,get_current_user: User = Depends(get_current_user)):
    return blog_handler.create_blog(blog)

