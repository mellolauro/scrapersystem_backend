# api/services/scraper_service.py

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any

from api.models.search_request import SearchRequest
from api.models.job_result import SystemResult
# Presumimos que score_service.py já foi ajustado para usar o campo 'detailed_content'
from api.services.score_service import calculate_system_score 

# Variável de Base URL para os links do MOCK
BASE_MOCK_URL = "http://ficticious-software-dir.com"

# --- FUNÇÃO DE SCRAPING DE DETALHES REAIS (SIMULADA) ---
def get_system_details_from_link(url: str) -> str:
    """
    Acessa a URL de detalhes do software e extrai o texto principal para análise.
    Retorna uma string vazia em caso de erro (que resultará em 0% de score).
    
    NOTA: Esta função é uma simulação da lógica de scraping real.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    
    print(f"DEBUG SCRAPER: Tentando acessar URL de detalhes: {url}")
    
    # ⚠️ Em um ambiente de produção, esta seria a lógica real de requisição:
    # try:
    #     response = requests.get(url, headers=headers, timeout=10)
    #     response.raise_for_status() 
    #     print(f"DEBUG SCRAPER: Status {response.status_code} para {url}")
    #     
    #     # Se o scraper precisar de extração mais específica (ex: BeautifulSoup)
    #     # soup = BeautifulSoup(response.text, 'html.parser')
    #     # return soup.find('main_description_div').get_text()
    #     
    # except requests.RequestException as e:
    #     print(f"ERROR SCRAPING DETALHES (Requisição falhou para {url}): {e}")
    #     return ""

    # --- MOCK DE COMPORTAMENTO PARA TESTAR OS 0% E OS >0% ---
    if "prorh" in url:
        # Simula a falha de acesso (403 Forbidden ou 404 Not Found), retornando vazio.
        print("DEBUG SCRAPER: Simulação de FALHA de acesso ao ProRH Manager. Retornando conteúdo VAZIO (0%).")
        return ""
        
    if "rhfacil" in url:
        # Simula o sucesso, fornecendo uma descrição que PONTUA contra os critérios (Recrutamento/Seleção).
        print("DEBUG SCRAPER: Simulação de SUCESSO. Retornando conteúdo pontuável.")
        return "Nossa solução é especializada em **recrutamento e seleção**, o que inclui recursos robustos para **triagem de candidatos por filtros** e **agendamento de entrevistas** em massa."
        
    if "totalrh" in url:
        # Simula um conteúdo que pontua apenas em parte (Folha de Pagamento)
        print("DEBUG SCRAPER: Simulação de SUCESSO. Retornando conteúdo parcialmente pontuável.")
        return "Sistema focado em processamento de **folha de pagamento** e gestão de benefícios."
        
    return ""

# --- FUNÇÃO DE SCRAPING DE BUSCA INICIAL (MOCK) ---
def perform_web_scraping(search_term: str) -> List[Dict[str, Any]]:
    """
    Simula o scraping de uma página de busca, retornando um mix de sistemas
    para que a Matriz de Aderência se encarregue de filtrar e classificar.
    """
    print(f"Buscando sistemas com termo: '{search_term}' (Simulação de Catálogo Completo)...")

    # --- SIMULANDO HTML de Busca ---
    mock_html = f"""
    <html><body>
        <div id="results">
            <div class="software-card">
                <h2 class="title">Sistema ProRH Manager</h2>
                <p class="company">Empresa A Software Ltda</p>
                <a href="/software/prorh">Ver Detalhes</a>
            </div>
            <div class="software-card">
                <h2 class="title">SalesMaster CRM</h2>
                <p class="company">CRM Experts</p>
                <a href="/software/salesmaster">Ver Detalhes</a>
            </div>
            <div class="software-card">
                <h2 class="title">Gestão Total RH</h2>
                <p class="company">Global Systems</p>
                <a href="/software/totalrh">Ver Detalhes</a>
            </div>
            <div class="software-card">
                <h2 class="title">Integrate ERP Pro</h2>
                <p class="company">Enterprise Solutions</p>
                <a href="/software/integrate">Ver Detalhes</a>
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
        
        if title_tag and company_tag and link_tag:
            system_link = BASE_MOCK_URL + link_tag['href']
            
            scraped_data.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "link": system_link,
            })
            
    return scraped_data

# --- FUNÇÃO ORQUESTRADORA (run_adherence_analysis) ---

def run_adherence_analysis(request: SearchRequest) -> List[SystemResult]:
    """Orquestra o scraping inicial, scraping de detalhes, pontuação e ranking."""
    
    # 1. Scraping Inicial (Lista de Sistemas)
    scraped_systems_data = perform_web_scraping(request.project_title)
    
    # 2. Pontuação
    results: List[SystemResult] = []
    
    # Calcula o score para cada sistema encontrado
    for system_data in scraped_systems_data:
        
        # OBTÉM O CONTEÚDO REAL DA PÁGINA DE DETALHES (Usando o link)
        detailed_content = get_system_details_from_link(system_data["link"])
        
        # Adiciona o conteúdo detalhado ao dict para ser usado na pontuação
        system_data["detailed_content"] = detailed_content 

        # A função calculate_system_score DEVE USAR detailed_content para pontuar
        # Nota: Você deve garantir que 'calculate_system_score' agora olhe para 'detailed_content'
        score, breakdown = calculate_system_score(
            request.adherence_matrix, 
            system_data,
        )
        
        results.append(SystemResult(
            title=system_data["title"],
            company=system_data["company"],
            link=system_data["link"],
            total_score=round(score, 2), # Arredonda para 2 casas
            adherence_breakdown=breakdown,
            ranking=0
        ))

    # 3. Ranking e Classificação
    results.sort(key=lambda x: x.total_score, reverse=True)
    
    for i, result in enumerate(results):
        result.ranking = i + 1
        
    return results