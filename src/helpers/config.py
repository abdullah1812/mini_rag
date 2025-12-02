from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "MyApp"
    APP_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(env_file=".env")

def get_setting():
    return Settings()