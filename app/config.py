from platform import version
from pydantic import BaseSettings


class Setting(BaseSettings):
    api_key: str
    url_instance: str
    version: str = version()
    api_key_text_speech: str
    url_instance_text_speech: str

    class Config:
        env_file = ".env"


settings = Setting()
