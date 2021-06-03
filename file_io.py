import json
from time import sleep
from os import access, R_OK


# Считывание всех тегов экспертной системы
def import_tags() -> list:
    question_path = f"tags.json"

    # Ожидание доступа к файлу
    while not access(question_path, R_OK):
        sleep(0.1)

    with open(question_path, encoding='utf-8') as q:
        raw = q.read()
    return _raw_json_to_dict(raw)['tags']


# Считывание с файла данных о вопросе в виде json. Файл формата question%qid%.json
def import_question_data(qid) -> dict:
    question_path = f"questions/question{qid}.json"

    # Ожидание доступа к файлу
    while not access(question_path, R_OK):
        sleep(0.1)

    with open(question_path, encoding='utf-8') as q:
        raw = q.read()
    return _raw_json_to_dict(raw)


# Считывание шаблона сессии (с весами 1)
def import_default_state() -> dict:
    default_state_path = f"sessions/session_pattern.json"

    # Ожидание доступа к файлу
    while not access(default_state_path, R_OK):
        sleep(0.1)

    with open(default_state_path, encoding='utf-8') as s:
        raw = s.read()
    return _raw_json_to_dict(raw)


# Считывание с файла состояния данной сессии в виде json. Файл формата session%qid%.json
def import_state(sid) -> dict:
    try:
        state_path = f"sessions/session{sid}.json"

        # Ожидание доступа к файлу
        while not access(state_path, R_OK):
            sleep(0.1)

        with open(state_path, encoding='utf-8') as s:
            raw = s.read()

        dct = _raw_json_to_dict(raw)
        assert dct['weights']
        assert dct['answered']
    except (json.decoder.JSONDecodeError, AssertionError):
        return import_default_state()
    return dct


# Запись файла состояния данной сессии в виде json. Файл формата session%qid%.json
def write_state(sid, dct):
    state_path = f"sessions/session{sid}.json"

    # Ожидание доступа к файлу
    while not access(state_path, R_OK):
        sleep(0.1)

    with open(state_path, mode='w', encoding='utf-8') as s:
        s.write(_json_to_string(dct))


# Преобразование json из вида строки в вид словаря
def _raw_json_to_dict(raw_str) -> dict:
    return json.loads(raw_str)


# Преобразование json из вида строки в вид словаря
def _json_to_string(dct) -> str:
    return json.dumps(dct, indent=4)


# Возвращает массив текущих активных сессий
def get_sessions_list():
    sessions_path = "sessions.json"

    # Ожидание доступа к файлу
    while not access(sessions_path, R_OK):
        sleep(0.1)

    with open(sessions_path, 'r', encoding='utf-8') as s:
        raw = s.read()

    return _raw_json_to_dict(raw)['sessions']


# Возвращает массив id всех вопросов из базы
def get_questions_list():
    questions_path = "questions.json"

    # Ожидание доступа к файлу
    while not access(questions_path, R_OK):
        sleep(0.1)

    with open(questions_path, 'r', encoding='utf-8') as s:
        raw = s.read()

    return _raw_json_to_dict(raw)['questions']
