FROM python:3.11-slim

WORKDIR /app

# Instala dependências
COPY api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia somente o código da API para dentro do container
COPY api /app/api

ENV PYTHONPATH=/app

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]
