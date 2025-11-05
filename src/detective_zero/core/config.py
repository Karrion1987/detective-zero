
from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "Detective Zero")
    env: str = os.getenv("ENV", "dev")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./detective_zero.db")

settings = Settings()
