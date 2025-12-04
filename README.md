1. Configuração e Credenciais (Sua Ação)
Para usar a API de Busca, você precisa obter duas informações cruciais no Google Cloud ou na plataforma de Busca Programável:
Chave de API (API_KEY): Sua credencial de acesso principal.
ID do Mecanismo de Busca Programável (CSE_ID): Um identificador que define qual motor de busca personalizado (Custom Search Engine) será usado para a consulta.
🛑 Importante: Segurança
Essas credenciais nunca devem ser codificadas diretamente no seu scraper_service.py. Elas devem ser passadas para o contêiner Docker via variáveis de ambiente.
Obtenha as chaves: Acesse o [Console do Google Cloud] para criar uma Chave de API e o [Motor de Busca Programável] para criar seu mecanismo de busca e obter o ID.
Atualize seu docker-compose.yml para incluir as variáveis no serviço api:
# docker-compose.yml (apenas o serviço 'api' modificado)
  api:
    build:
      context: .
      dockerfile: api/Dockerfile
    container_name: scraper_api
    # ... outras configurações ...
    environment:
      - PYTHONPATH=/app
      - GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI
      - GOOGLE_CSE_ID=SEU_ID_DO_MOTOR_DE_BUSCA_AQUI
    # ...

Ótima escolha! Avançar com a integração da API de Busca Personalizada do Google (Custom Search API - CSE) é a maneira correta e profissional de realizar a busca em tempo real para seu sistema.

A integração exige três etapas: Configuração de Credenciais, Instalação da Biblioteca e Modificação do Código Python.

1. Configuração e Credenciais (Sua Ação)
Para usar a API de Busca, você precisa obter duas informações cruciais no Google Cloud ou na plataforma de Busca Programável:

Chave de API (API_KEY): Sua credencial de acesso principal.

ID do Mecanismo de Busca Programável (CSE_ID): Um identificador que define qual motor de busca personalizado (Custom Search Engine) será usado para a consulta.

🛑 Importante: Segurança
Essas credenciais nunca devem ser codificadas diretamente no seu scraper_service.py. Elas devem ser passadas para o contêiner Docker via variáveis de ambiente.

Obtenha as chaves: Acesse o [Console do Google Cloud] para criar uma Chave de API e o [Motor de Busca Programável] para criar seu mecanismo de busca e obter o ID.

Atualize seu docker-compose.yml para incluir as variáveis no serviço api:

YAML

# docker-compose.yml (apenas o serviço 'api' modificado)
  api:
    build:
      context: .
      dockerfile: api/Dockerfile
    container_name: scraper_api
    # ... outras configurações ...
    environment:
      - PYTHONPATH=/app
      - GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI
      - GOOGLE_CSE_ID=SEU_ID_DO_MOTOR_DE_BUSCA_AQUI
    # ...
-----------------------------------------------------------------------------------------------------------------------------------------------------
2. Instalação da Biblioteca Python
Você precisa da biblioteca oficial do Google para interagir com a API.

Execute este comando dentro do seu ambiente Python local ou adicione ao seu Dockerfile da API: Ótima escolha! Avançar com a integração da API de Busca Personalizada do Google (Custom Search API - CSE) é a maneira correta e profissional de realizar a busca em tempo real para seu sistema.

A integração exige três etapas principais: Configuração de Credenciais, Instalação da Biblioteca e Modificação do Código Python.

1. Configuração e Credenciais (Sua Ação)
Para usar a API de Busca, você precisa obter duas informações cruciais no Google Cloud ou na plataforma de Busca Programável:

Chave de API (API_KEY): Sua credencial de acesso principal.

Você deve obtê-la no [Google Cloud Console], criando um projeto e depois navegando para APIs & Services > Credentials (Credenciais) e gerando uma nova chave de API.

Certifique-se de ativar a "Custom Search API" para o seu projeto no Google Cloud Console.

ID do Mecanismo de Busca Programável (CSE_ID ou cx): Um identificador que define qual motor de busca personalizado será usado para a consulta.

Você deve criar este motor em [Google Programmable Search Engine] e pode configurá-lo para pesquisar a Web inteira.

🛑 Importante: Segurança
Essas credenciais nunca devem ser codificadas diretamente no seu scraper_service.py. Elas devem ser passadas para o contêiner Docker via variáveis de ambiente.
Atualize seu docker-compose.yml para incluir as variáveis no serviço api:

2. Instalação da Biblioteca Python
Você precisa da biblioteca oficial do Google para interagir com a API.

Adicione a biblioteca ao seu #Dockerfile da API ou execute a instalação manualmente se estiver em ambiente de desenvolvimento local:
# Adicione esta linha ao seu Dockerfile da API, antes de instalar dependências
RUN pip install google-api-python-client
# ou, se estiver no seu terminal Python local
# pip install google-api-python-client
A biblioteca principal é google-api-python-client.

Ótima escolha! Avançar com a integração da API de Busca Personalizada do Google (Custom Search API - CSE) é a maneira correta e profissional de realizar a busca em tempo real para seu sistema.

A integração exige três etapas: Configuração de Credenciais, Instalação da Biblioteca e Modificação do Código Python.

1. Configuração e Credenciais (Sua Ação)
Para usar a API de Busca, você precisa obter duas informações cruciais no Google Cloud ou na plataforma de Busca Programável:

Chave de API (API_KEY): Sua credencial de acesso principal.

ID do Mecanismo de Busca Programável (CSE_ID): Um identificador que define qual motor de busca personalizado (Custom Search Engine) será usado para a consulta.

🛑 Importante: Segurança
Essas credenciais nunca devem ser codificadas diretamente no seu scraper_service.py. Elas devem ser passadas para o contêiner Docker via variáveis de ambiente.

Obtenha as chaves: Acesse o [Console do Google Cloud] para criar uma Chave de API e o [Motor de Busca Programável] para criar seu mecanismo de busca e obter o ID.

Atualize seu docker-compose.yml para incluir as variáveis no serviço api:

YAML

# docker-compose.yml (apenas o serviço 'api' modificado)
  api:
    build:
      context: .
      dockerfile: api/Dockerfile
    container_name: scraper_api
    # ... outras configurações ...
    environment:
      - PYTHONPATH=/app
      - GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI
      - GOOGLE_CSE_ID=SEU_ID_DO_MOTOR_DE_BUSCA_AQUI
    # ...
2. Instalação da Biblioteca Python
Você precisa da biblioteca oficial do Google para interagir com a API.

Execute este comando dentro do seu ambiente Python local ou adicione ao seu Dockerfile da API: Ótima escolha! Avançar com a integração da API de Busca Personalizada do Google (Custom Search API - CSE) é a maneira correta e profissional de realizar a busca em tempo real para seu sistema.

A integração exige três etapas principais: Configuração de Credenciais, Instalação da Biblioteca e Modificação do Código Python.

1. Configuração e Credenciais (Sua Ação)
Para usar a API de Busca, você precisa obter duas informações cruciais no Google Cloud ou na plataforma de Busca Programável:

Chave de API (API_KEY): Sua credencial de acesso principal.

Você deve obtê-la no [Google Cloud Console], criando um projeto e depois navegando para APIs & Services > Credentials (Credenciais) e gerando uma nova chave de API.

Certifique-se de ativar a "Custom Search API" para o seu projeto no Google Cloud Console.

ID do Mecanismo de Busca Programável (CSE_ID ou cx): Um identificador que define qual motor de busca personalizado será usado para a consulta.

Você deve criar este motor em [Google Programmable Search Engine] e pode configurá-lo para pesquisar a Web inteira.

🛑 Importante: Segurança
Essas credenciais nunca devem ser codificadas diretamente no seu scraper_service.py. Elas devem ser passadas para o contêiner Docker via variáveis de ambiente.

Atualize seu docker-compose.yml para incluir as variáveis no serviço api:

YAML

# docker-compose.yml (apenas o serviço 'api' modificado)
  api:
    build:
      context: .
      dockerfile: api/Dockerfile
    container_name: scraper_api
    # ... outras configurações ...
    environment:
      - PYTHONPATH=/app
      - GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI
      - GOOGLE_CSE_ID=SEU_ID_DO_MOTOR_DE_BUSCA_AQUI
    # ...
2. Instalação da Biblioteca Python
Você precisa da biblioteca oficial do Google para interagir com a API.

Adicione a biblioteca ao seu Dockerfile da API ou execute a instalação manualmente se estiver em ambiente de desenvolvimento local:

Bash

# Adicione esta linha ao seu Dockerfile da API, antes de instalar dependências
RUN pip install google-api-python-client
# ou, se estiver no seu terminal Python local
# pip install google-api-python-client
A biblioteca principal é google-api-python-client.

3. Modificação do Código em scraper_service.py
Vamos refatorar a função perform_web_scraping para chamar a API real e a função get_system_details_from_link para fazer o scraping do link real.
Código Refatorado para Busca Real

# api/services/scraper_service.py

import requests
import os # Importar para ler variáveis de ambiente
from googleapiclient.discovery import build # Importação crucial para a API
from typing import List, Dict, Any
# ... (outras importações) ...

# 1. Obter credenciais do ambiente (Docker)
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

# --- FUNÇÃO DE BUSCA REAL (API GOOGLE) ---
def perform_web_scraping(search_term: str) -> List[Dict[str, Any]]:
    """
    Executa uma busca real usando a API Custom Search do Google.
    """
    if not API_KEY or not CSE_ID:
        print("ERRO: Credenciais da API Google não configuradas. Retornando MOCK de Falha.")
        # Retorna lista vazia ou mock de erro
        return [] 
        
    print(f"Buscando sistemas com termo: '{search_term}' via API Google...")

    try:
        # 1. Inicializa o serviço da API
        service = build("customsearch", "v1", developerKey=API_KEY)
        
        # 2. Executa a busca. 'q' é a query, 'cx' é o CSE ID.
        res = service.cse().list(
            q=f'"{search_term}" software', # Busca por software com o termo exato
            cx=CSE_ID,
            num=5 # Retorna os 5 primeiros resultados
        ).execute()

        scraped_data: List[Dict[str, Any]] = []
        for item in res.get('items', []):
            scraped_data.append({
                "title": item.get('title'),
                "company": item.get('displayLink'), # O nome do domínio pode servir como 'Empresa'
                "link": item.get('link'),
            })
        
        return scraped_data

    except Exception as e:
        print(f"ERRO CRÍTICO na API do Google Search: {e}")
        return []

# --- FUNÇÃO DE SCRAPING DE DETALHES (Varredura do Link Real) ---
def get_system_details_from_link(url: str) -> str:
    """
    Tenta acessar a URL real e raspar o conteúdo para análise.
    ⚠️ Esta é a parte de Web Scraping que pode ser BLOCKEADA.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    
    print(f"DEBUG SCRAPER: Varrendo URL de detalhes REAL: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Lança exceção para erros HTTP (4xx ou 5xx)
        
        # Usa BeautifulSoup para extrair todo o texto (sem tags)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tenta remover scripts e estilos para limpar o texto
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
            
        text = soup.get_text()
        
        # Limpa espaços e novas linhas
        return " ".join(text.split()).lower()

    except requests.RequestException as e:
        print(f"ERROR SCRAPING DETALHES (Requisição falhou para {url}): {e}")
        # Retorna vazio se o site bloquear ou não existir (resulta em 0% de aderência)
        return ""

# ... (A função run_adherence_analysis permanece a mesma, pois ela chama as duas funções acima) ...
4. Últimos Passos
Obtenha suas Credenciais (API Key e CSE ID).
Atualize seu docker-compose.yml com as variáveis de ambiente (Substitua SUA_CHAVE_DE_API_AQUI e SEU_ID_DO_MOTOR_DE_BUSCA_AQUI).
Atualize o Dockerfile para incluir a biblioteca google-api-python-client.
Substitua o conteúdo do scraper_service.py pelo código acima.
Reconstrua e Inicie:
docker compose down
docker compose build api # Para instalar a nova biblioteca
docker compose up -d
