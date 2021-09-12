from flask import *
from database_api import *


app = Flask(__name__)


@app.route('/undefined/login', methods=['POST'])
def login():
    value = request.get_json(silent=True)
    if authorize_user(value['email'], value['password']) == [(1,)]:
        result = select_user_data(value['email'])
        dictionary_for_work = {}
        dictionary_for_work.update({'200': result})
        return dictionary_for_work
    else:
        print('Неверный логин или пароль')
        return '400'


@app.route('/sign/up/undefined/registration', methods=['POST'])
def registration_page2():
    value = request.get_json(silent=True)
    if authorize_user(value['email'], value['password']) != [(1,)]:
        add_new_user(value['email', value['password'], value['firsName'], value['secondName'], value['thirdName'], value['university']])
        return '200'
    else:
        return '400'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
