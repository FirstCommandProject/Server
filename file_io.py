import json
from time import sleep
from os import access, R_OK


# Считывание с файла данных о вопросе в виде json. Файл формата question%qid%.json
def import_question_data(qid) -> str:
    question_path = f"questions/question{qid}.json"

    # Ожидание доступа к файлу
    while not access(question_path, R_OK):
        sleep(0.1)

    with open(question_path, encoding='utf-8') as q:
        raw = q.read()
    return raw


# Считывание с файла состояния данной сессии в виде json. Файл формата session%qid%.json
def import_state(sid) -> str:
    state_path = f"sessions/session{sid}.json"

    # Ожидание доступа к файлу
    while not access(state_path, R_OK):
        sleep(0.1)

    with open(state_path, encoding='utf-8') as s:
        raw = s.read()
    return raw


# Запись файла состояния данной сессии в виде json. Файл формата session%qid%.json
def write_state(sid, raw):
    state_path = f"sessions/session{sid}.json"

    # Ожидание доступа к файлу
    while not access(state_path, R_OK):
        sleep(0.1)

    with open(state_path, mode='w', encoding='utf-8') as s:
        s.write(raw)


# Преобразование json из вида строки в вид словаря
def raw_json_to_dict(raw_str) -> dict:
    return json.loads(raw_str)


# Преобразование json из вида строки в вид словаря
def json_to_string(dct) -> str:
    return json.dumps(dct, indent=4)


# Возвращает массив текущих активных сессий
def get_sessions_list():
    sessions_path = "sessions.json"

    # Ожидание доступа к файлу
    while not access(sessions_path, R_OK):
        sleep(0.1)

    with open(sessions_path, 'r', encoding='utf-8') as s:
        raw = s.read()

    return raw_json_to_dict(raw)['sessions']


# Возвращает массив id всех вопросов из базы
def get_questions_list():
    questions_path = "questions.json"

    # Ожидание доступа к файлу
    while not access(questions_path, R_OK):
        sleep(0.1)

    with open(questions_path, 'r', encoding='utf-8') as s:
        raw = s.read()

    return raw_json_to_dict(raw)['questions']
