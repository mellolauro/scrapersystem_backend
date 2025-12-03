from pydantic import BaseModel
from typing import Dict, Any, List

class AdherenceDetail(BaseModel):
    """Detalhes de aderência de uma característica específica."""
    feature_description: str 
    is_present: bool         
    score_contribution: float 

class SystemResult(BaseModel):
    """Modelo para um único resultado de software com sua pontuação e ranking."""
    title: str               
    company: str             
    link: str                
    total_score: float       
    ranking: int             
    adherence_breakdown: List[AdherenceDetail] 