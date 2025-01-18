from pydantic import BaseModel


class Killers(BaseModel):
    killers: list[int]