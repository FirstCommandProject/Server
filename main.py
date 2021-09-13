from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database_api.database_api import *
import uvicorn
from models import *

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

@app.post('/login', status_code=200)
async def login(body: LoginModel):
    if authorize_user(body.email, body.password) == [(1,)]:
        result=select_user_data(body.email)
        result_dictionary={}
        result_dictionary.update(
            statusCode='200', 
            data=result[0]
        )
        return result_dictionary
    else:
        print('Ошибка входа')
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")


@app.post('/registration', status_code=200)
async def registration(body: RegistrModel):

    if authorize_user(body.email, body.password) != [(1,)]:
        result=add_new_user(body.email, body.password, body.firstName, body.secondName, body.thirdName, body.university)
        result_dictionary={}
        # TO-DO: return user in after_new_user function
        result=select_user_data(body.email)
        result_dictionary.update(
            statusCode='200', 
            data=result[0]
        )
        return result_dictionary
    else:
        print('Ошибка регистрации')
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует")


if __name__ == "__main__":
    uvicorn.run('main:app', port=5000, reload=True)
