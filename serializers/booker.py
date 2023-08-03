import typing as t
from pydantic import BaseModel, Field

class Token(BaseModel):
    token: str = Field(...)


