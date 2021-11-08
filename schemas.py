from pydantic import BaseModel


class FaceSchema(BaseModel):
    image: str
