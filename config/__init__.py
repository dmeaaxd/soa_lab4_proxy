from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    SOAP_SERVICE_URL: str


configuration = Settings()
