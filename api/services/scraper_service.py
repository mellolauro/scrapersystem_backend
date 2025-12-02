import requests
from bs4 import BeautifulSoup

def google_search(query: str):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}+software"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    for g in soup.select(".tF2Cxc"):
        title = g.select_one(".DKV0Md")
        link = g.select_one("a")

        if title and link:
            results.append({
                "title": title.text,
                "url": link["href"]
            })

    return results


# 🚀 Função chamada pelo worker de fila
def run_scraper_job(payload: dict):
    query = payload.get("query") or payload.get("title")

    if not query:
        return {"error": "Nenhuma query foi enviada."}

    results = google_search(query)
    return {"query": query, "results": results}

def run_scraper_job(data):
    print("JOB RECEIVED:", data)
    return {"ok": True}