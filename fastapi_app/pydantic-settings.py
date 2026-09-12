from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Clean API"
    API_V1_STR: str = "/api/v1"

    # Reads variables from a local .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()