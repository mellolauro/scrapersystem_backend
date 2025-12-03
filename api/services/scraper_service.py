import requests
from bs4 import BeautifulSoup

def search_softwares(query: str):
    """
    Busca softwares relacionados no Google e extrai título, url,
    empresa (se possível) e descrição básica.
    """
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}+software"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    for g in soup.select(".tF2Cxc"):
        title = g.select_one(".DKV0Md")
        link = g.select_one("a")
        snippet = g.select_one(".VwiC3b")

        if not title or not link:
            continue

        results.append({
            "name": title.text.strip(),
            "description": snippet.text.strip() if snippet else "",
            "company": "Desconhecido",
            "url": link["href"]
        })

    return results
