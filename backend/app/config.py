from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "user"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "mydb"
    
    class Config:
        env_file = ".env"

settings = Settings()
