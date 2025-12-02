from pydantic import BaseModel
from typing import List

class SearchRequest(BaseModel):
    title: str
    requirements: List[str]
