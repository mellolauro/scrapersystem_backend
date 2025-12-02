from pydantic import BaseModel

class JobResult(BaseModel):
    source: str
    score: float
    url: str
    snippet: str
