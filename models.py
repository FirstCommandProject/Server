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