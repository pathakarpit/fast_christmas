import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Fast Christmas"
    API_KEY: str = os.getenv("API_KEY", "demo-key")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "secret")
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    MODEL_PATH: str = "app/models/model.joblib"

settings = Settings()