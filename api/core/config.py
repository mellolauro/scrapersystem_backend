import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "ScraperSystem"
    ENV: str = os.getenv("ENV", "development")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")

settings = Settings()
