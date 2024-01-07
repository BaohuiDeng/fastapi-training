from fastapi import HTTPException
from fastapi_training.database import fastapi_training
from fastapi_training.model.blog import Blog

def get_all_blogs():
    blogs_cursor = fastapi_training.blogs.find()
    if blogs_cursor is None:
        raise  HTTPException(status_code=404, detail="No blogs found")
    
    blogs = []
    for blog in blogs_cursor:
        blog['_id'] = str(blog['_id'])
        blogs.append(blog)
    return blogs


def get_blog_by_id(id:int):
    blog = fastapi_training.blogs.find_one({"id": id})
    blog['_id'] = str(blog['_id'])
    if blog:
        return blog
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
    

def create_blog(blog:Blog):
    result = fastapi_training.blogs.insert_one(blog.model_dump())
    if result.inserted_id:
        return {"message": "Blog created successfully", "blog_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create blog")