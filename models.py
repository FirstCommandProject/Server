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
    title: str
    university: str
    firstData: str
    secondData: str
    weights: dict


class QuestionModel(BaseModel):
    id: int


class ResultModel(BaseModel):
    email: str


class UserSessionDataModel(BaseModel):
    weights: dict
    answered: list


class AnswerQuestion(BaseModel):
    session: str
    id: int
    answer: int
