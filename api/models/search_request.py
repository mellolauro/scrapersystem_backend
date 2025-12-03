from pydantic import BaseModel
from typing import List

class Feature(BaseModel):
    """Modelo para um único critério de aderência com peso."""
    description: str  
    weight: int       

class SearchRequest(BaseModel):
    """Modelo da requisição de busca do usuário."""
    project_title: str       
    adherence_matrix: List[Feature] 