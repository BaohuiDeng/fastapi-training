from pydantic import BaseModel

class Blog(BaseModel):
    id:int
    title: str
    description: str
    published_at: str