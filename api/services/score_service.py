
from typing import List, Dict, Any, Tuple 
from api.models.search_request import Feature
from api.models.job_result import AdherenceDetail



def calculate_system_score(
    adherence_matrix: List[Feature], 
    system_data: Dict[str, Any]
) -> Tuple[float, List[AdherenceDetail]]:
    
    total_score = 0.0
    # Calcula a pontuação máxima possível (ex: soma dos pesos * 10)
    total_max_score = sum(feature.weight * 10 for feature in adherence_matrix) 
    adherence_breakdown: List[AdherenceDetail] = []
    
    # Pega a descrição do sistema em minúsculas para comparação
    system_description_lower = system_data.get("detailed_content", "").lower()
    
    for feature in adherence_matrix:
        feature_text = feature.description.lower()
        
        # Lógica de Aderência Real: Verifica se o texto do requisito (feature)
        # está contido na descrição do software raspada.
        is_present = feature_text in system_description_lower
        
        # Pontuação concedida: (10 pontos se presente) x Peso definido pelo usuário
        score_granted = feature.weight * (10 if is_present else 0)
        total_score += score_granted
        
        adherence_breakdown.append(AdherenceDetail(
            feature_description=feature.description,
            is_present=is_present,
            score_contribution=score_granted
        ))

    # Normaliza o score para uma base de 100%
    if total_max_score > 0:
        normalized_score = (total_score / total_max_score) * 100
    else:
        normalized_score = 0
        
    return normalized_score, adherence_breakdown