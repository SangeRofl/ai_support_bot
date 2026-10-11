from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):

    BOT_TOKEN: SecretStr


    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra='ignore')



settings = Settings()