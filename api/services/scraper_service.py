# api/services/scraper_service.py
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any

from api.models.search_request import SearchRequest
from api.models.job_result import SystemResult
from api.services.score_service import calculate_system_score

# --- FUNÇÃO DE SCRAPING REAL ---
def perform_web_scraping(search_term: str) -> List[Dict[str, Any]]:
    """
    Realiza o scraping de uma página de busca fictícia (ou real).
    
    NOTA IMPORTANTE: A URL deve ser substituída por um alvo real
    e a estrutura de parsing deve ser adaptada ao HTML real do site.
    Este é um MOCK de estrutura de site.
    """
    # 1. Adaptar a URL de busca (Exemplo Fictício de um site de comparação)
    # Em um cenário real, você codificaria o 'search_term' e o adicionaria ao URL
    # Ex: url = f"http://ficticious-software-dir.com/search?q={search_term.replace(' ', '+')}"
    
    # Usaremos uma URL de MOCK para demonstração, já que não temos um site real alvo
    # Em uma implementação real, você faria uma requisição real:
    # response = requests.get(url) 
    
    print(f"Buscando sistemas com termo: '{search_term}'...")

    # --- SIMULANDO HTML de Busca ---
    # Imagine que esta é a resposta HTTP de um site de busca por software
    mock_html = f"""
    <html><body>
        <div id="results">
            <div class="software-card">
                <h2 class="title">Sistema ProRH Manager</h2>
                <p class="company">Empresa A Software Ltda</p>
                <a href="/software/prorh">Ver Detalhes</a>
                <p class="description">Solução completa com **folha de pagamento automatizada**, gestão de ponto e integração com bancos.</p>
            </div>
            <div class="software-card">
                <h2 class="title">RH Fácil Cloud</h2>
                <p class="company">FácilTech Inovações</p>
                <a href="/software/rhfacil">Ver Detalhes</a>
                <p class="description">Focado em **recrutamento e seleção**, onboarding digital e treinamento online. Sem folha de pagamento.</p>
            </div>
            <div class="software-card">
                <h2 class="title">Gestão Total RH</h2>
                <p class="company">Global Systems</p>
                <a href="/software/totalrh">Ver Detalhes</a>
                <p class="description">Abrangente: possui ponto eletrônico, gestão de benefícios e **motor de cálculo de imposto**.</p>
            </div>
        </div>
    </body></html>
    """
    
    # 2. Parsing do HTML
    soup = BeautifulSoup(mock_html, 'html.parser')
    scraped_data: List[Dict[str, Any]] = []
    
    for card in soup.select('.software-card'):
        title_tag = card.select_one('.title')
        company_tag = card.select_one('.company')
        link_tag = card.select_one('a')
        description_tag = card.select_one('.description')
        
        if title_tag and company_tag and link_tag and description_tag:
            system_link = "http://ficticious-software-dir.com" + link_tag['href']
            
            scraped_data.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "link": system_link,
                # A descrição é crucial para o cálculo do score
                "description": description_tag.text.strip() 
            })
            
    return scraped_data

# --- FUNÇÃO ORQUESTRADORA (run_adherence_analysis) ---

def run_adherence_analysis(request: SearchRequest) -> List[SystemResult]:
    """Orquestra o scraping, pontuação e ranking."""
    
    # 1. Scraping (Chamada da função real/simulada)
    scraped_systems_data = perform_web_scraping(request.project_title)
    
    # 2. Pontuação
    results: List[SystemResult] = []
    
    # Calcula o score para cada sistema encontrado
    for system_data in scraped_systems_data:
        # A função calculate_system_score usa a descrição do sistema para pontuar.
        score, breakdown = calculate_system_score(
            request.adherence_matrix, 
            system_data
        )
        
        results.append(SystemResult(
            title=system_data["title"],
            company=system_data["company"],
            link=system_data["link"],
            total_score=round(score, 2), # Arredonda para 2 casas
            adherence_breakdown=breakdown,
            ranking=0 # Será preenchido na próxima etapa
        ))

    # 3. Ranking e Classificação
    # Ordena os resultados pelo score de forma decrescente
    results.sort(key=lambda x: x.total_score, reverse=True)
    
    # Atribui a posição no ranking
    for i, result in enumerate(results):
        result.ranking = i + 1
        
    return results