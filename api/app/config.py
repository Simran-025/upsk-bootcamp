from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    port: int = Field(..., env="PORT")

    @validator("port")
    def validate_port(cls, v):
        if v < 1 or v > 65535 or v > 65535:
            raise ValueError("PORT must be between 1 and 65535")
        return v

settings = Settings()
