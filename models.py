from pydantic import BaseModel
import json
import time


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


class QuestionModel(BaseModel):
    id: int


class ResultModel(BaseModel):
    email: str


class UserSessionDataModel(BaseModel):
    weights: dict
    answered: list


class AnswerQuestion(BaseModel):
    session: dict
    id: int
    answer: int


class UpdateUserData(BaseModel):
    login: str
    new_login: str
    new_password: str
    new_name: str
    new_surname: str
    new_patronymic: str
    new_university: str
