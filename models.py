from pydantic import BaseModel


class LoginModel(BaseModel):
    email: str
    password: str


class RegistrModel(BaseModel):
    email: str
    password: str
    firstName: str
    secondName: str
    thirdName: str
    university: str


class CafedraModel(BaseModel):
    id: int
    title: str
    university: str
    firstData: str
    secondData: str
    weights: dict
