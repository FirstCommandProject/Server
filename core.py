import json
import sys
from os import access, R_OK
from time import sleep


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


# Нормализует веса в состоянии по принципу нормализации вектора
def normalize_state(st):
    max_weight = 0
    for key in st['weights'].keys():
        max_weight = max(max_weight, st['weights'][key])
    if max_weight == 0:
        return
    for key in st['weights'].keys():
        st['weights'][key] /= max_weight


# Возвращает массив текущих активных сессий
def get_sessions_list():
    sessions_path = "sessions.json"

    # Ожидание доступа к файлу
    while not access(sessions_path, R_OK):
        sleep(0.1)

    with open(sessions_path, 'r', encoding='utf-8') as s:
        raw = s.read()

    return raw_json_to_dict(raw)['sessions']


# Ratio 1 - полностью применить. Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 2
# Ratio 0 - ничего не применять
# Ratio -1 - применить в обратную сторону.
# Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 0.5
def apply_question_to_state(qu, st, rt=1):
    if rt == 0:
        return
    question_keys = qu['weights'].keys()
    for key in question_keys:
        if st['weights'].get(key):
            if rt > 0:
                st['weights'][key] *= qu['weights'][key]
            else:
                st['weights'][key] /= qu['weights'][key]


# Первый аргумент:
# -a <session_id> <question_id> <ratio> применить влияние вопроса на результат с коэф. ratio
# (см. функцию apply_question_to_state)
#
# TODO -delete <session_id> удалить сессию
# TODO -new <session_id> создать сессию
if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == '-update':
        session_id = int(sys.argv[2])
        question_id = int(sys.argv[3])
        ratio = int(sys.argv[4])

        state = raw_json_to_dict(import_state(session_id))
        question = raw_json_to_dict(import_question_data(question_id))
        apply_question_to_state(question, state, ratio)
        normalize_state(state)
        write_state(session_id, json_to_string(state))
    else:
        print('Ошибка: неизвестный аргумент')
