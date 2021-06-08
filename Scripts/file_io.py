import json
from time import sleep
from os import access, R_OK


# TODO получать с базы данных
def _get_question_from_database(qid) -> dict:
    # Работа с API
    # question_path = f"questions/question{qid}.json"
    #
    # with open(question_path, encoding='utf-8') as q:
    #     raw = q.read()
    # return _raw_json_to_dict(raw)
    pass


# TODO получать с сервера
# Считывание шаблона сессии (с весами 1)
def import_default_state() -> dict:
    default_state_path = f"sessions/session_pattern.json"

    with open(default_state_path, encoding='utf-8') as s:
        raw = s.read()
    return _raw_json_to_dict(raw)


def import_state(sid) -> dict:
    try:
        raw = ''
        # TODO работа с API
        dct = _raw_json_to_dict(raw)
        assert dct['weights']
        assert dct['answered']
    except (json.decoder.JSONDecodeError, AssertionError):
        return import_default_state()
    return dct


# TODO
# Возвращает состояние
def return_state(dct):
    return dct


# Преобразование json из вида строки в вид словаря
def _raw_json_to_dict(raw_str) -> dict:
    return json.loads(raw_str)


# Преобразование json из вида строки в вид словаря
def _json_to_string(dct) -> str:
    return json.dumps(dct, indent=4)
