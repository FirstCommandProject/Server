from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database_api.database_api import *
import uvicorn
from models import *
from scripts.core import *
import json
import time
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

session_pattern = {
    "weights": {
            "math":1,
            "astronomy":1,
            "programming":1, 
            "informatics":1, 
            "psychology":1, 
            "linguistics":1,
            "economy":1, 
            "geography":1, 
            "biology":1,
            "anatomy":1,
            "religious studies":1,
            "political science":1,
            "chemistry":1,
            "business":1,
            "engineering":1  
    },
    "answered": []
}

@app.post('/login', status_code=200)
async def login(body: LoginModel):
    if authorize_user(body.email, body.password) == [(1,)]:
        result=select_user_data(body.email)
        result_dictionary={}
        result_dictionary.update(
            statusCode='200',
            data=result
        )
        return result_dictionary
    else:
        print('Ошибка входа')
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")


@app.post('/registration', status_code=200)
async def registration(body: RegistrModel):

    if authorize_user(body.email, body.password) != [(1,)]:
        add_new_user(body.email, body.password, body.firstName, body.secondName, body.thirdName, body.university)
        result = select_user_data(body.email)
        result_dictionary = {}
        result_dictionary.update(
            statusCode='200',
            data=result
        )
        return result_dictionary
    else:
        print('Ошибка регистрации')
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует")


@app.post('/departments', status_code=200)
async def departments(body:CafedraModel):
    if select_cafedra_by_id(body.id):
        result = select_user_data(body.email)
        result_dictionary = {}
        result_dictionary.update(
            statusCode='200',
            data=result
        )
        return result_dictionary
    else:
        select_cafedras()
        raise HTTPException(status_code=400, detail="Такой кафедры не существует")

#получение вопроса
@app.post('/test', status_code=200)
async def questionreturn(body:QuestionModel):
    if select_question_by_id(body.id):
        result = select_question_by_id(body.id)
        result_dictionary = {}
        result_dictionary.update(
            statusCode='200',
            data=result
        )
        return result_dictionary
    else:
        print('Ошибка получения вопроса')
        raise HTTPException(status_code=400, detail='Такого вопроса не существует')

#получение релевантного вопроса
@app.post('/relevant-question', status_code=200)
async def get_relevant_question(body:UserSessionDataModel):
    dictionary = {'weights': body.weights, 'answered': body.answered}
    result_question = choose_relevant_question(dictionary)
    result_dictionary = {}
    result_dictionary.update(
        statusCode='200',
        data=result_question
    )
    return result_dictionary

#получение начальных настроек
@app.get('/default-session', status_code=200)
async def sessiondeault():
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=session_pattern
    )
    return dictionary

#обработка ответа
@app.post('/answer-question', status_code=200)
async def answerquestion(body:AnswerQuestion):
    dictionary = {}
    new_session = update_weights(body.session, body.id, body.answer)
    dictionary.update(
        statusCode='200',
        data=new_session
    )
    return dictionary


if __name__ == "__main__":
    uvicorn.run('main:app', port=5000, reload=True)
