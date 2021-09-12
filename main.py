from flask import *
from database_api import *
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    value = request.get_json(silent=True)
    if authorize_user(value['email'], value['password']) == [(1,)]:
        result = select_user_data(value['email'])
        dictionary_for_work = {}
        dictionary_for_work.update({'200': result})
        return dictionary_for_work
    else:
        print('Неверный логин или пароль')
        return abort(400)


@app.route('/sign/up/undefined/registration', methods=['POST'])
@cross_origin()
def registration_page2():
    value = request.get_json(silent=True)
    if authorize_user(value['email'], value['password']) != [(1,)]:
        add_new_user(value['email', value['password'], value['firsName'], value['secondName'], value['thirdName'], value['university']])
        return '200'
    else:
        return abort(400)


if __name__ == "__main__":
    app.run(debug=False)
