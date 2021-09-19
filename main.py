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
    if body.id:
        if select_cafedra_by_id(body.id):
            result = select_user_data(body.id)
            result_dictionary = {}
            result_dictionary.update(
                statusCode='200',
                data=result
            )
            return result_dictionary
        else:
            raise HTTPException(status_code=400, detail="Такой кафедры не существует")
    else:
        select_cafedras()


@app.get('/test', status_code=200)
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
        print('Ошибка')
        raise HTTPException(status_code=400, detail='Такого вопроса не существует')


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


@app.get('/default-session', status_code=200)
async def sessiondeault():
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=session_pattern
    )
    return dictionary


@app.post('/answer-question', status_code=200)
async def answerquestion(body:AnswerQuestion):
    dictionary = {}
    new_session = update_weights(body.session, body.id, body.answer)
    dictionary.update(
        statusCode='200',
        data=new_session
    )
    return dictionary


@app.post('/new-user-data', status_code=200)
async def changeuserdata(body:UpdateUserData):
    if update_user_data(body.login, body.new_login, body.new_password, body.new_name, body.new_surname, body.new_patronymic, body.new_university) == [0]:
        dictionary = {}
        dictionary.update(
            statusCode='200',
            data=select_user_data(body.login)
        )
        return dictionary
    else:
        print('Ошибка')
        raise HTTPException(status_code=400, detail='Такого пользователя не существует')


@app.post('/restore-password', status_code=200)
async def restorepassword(body:RestorePassword):
    restore_user_password(body.login, body.password)
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=select_user_data(body.login)
    )
    return dictionary


@app.post('/take-user-data', status_code=200)
async def takeuserdata(body:ResultModel):
    result = select_user_data(body.email)
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=result
    )
    return dictionary


@app.post('/last-user-answer', status_code=200)
async def lastuseranswer(body:LastAnswer):
    insert_table_results(body.login, body.session, body.time)
    dictionary = {}
    dictionary.update(
        statusCode='200'
    )


@app.post('/last-user-result', status_code=200)
async def lastuserresult(body:LastResult):
    result = select_last_result()
    dictionary = {}
    dictionary.update(
        statusCode='200',
        data=result
    )
    return dictionary


if __name__ == "__main__":
    uvicorn.run('main:app', port=5000, reload=True)
