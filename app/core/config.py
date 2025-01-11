from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    api_key: str = Field(default='api_key', alias='API_KEY')

    db_user: str = Field(default='db_user', alias='DB_USER')
    db_password: str = Field(default='db_password', alias='DB_PASSWORD')
    db_host: str = Field(default='db_host', alias='DB_HOST')
    db_name: str = Field(default='db_name', alias='DB_NAME')
    db_port: int = Field(default=5432, alias='DB_PORT')


settings = Config()
