from platform import version
from pydantic import BaseSettings


class Setting(BaseSettings):
    api_key: str
    url_instance: str
    version: str = version()

    class Config:
        env_file = ".env"

settings = Setting()
