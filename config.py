from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "planner-api"
    database_url: str
    redis_url: str = "redis://redis:6379/0"
    here_api_key: str = "CHANGEME"

    class Config:
        env_file = ".env"

settings = Settings()
