import sys
from file_io import *
from question_chooser import *


# Возврат любого значения из программы
def emit(message):
    print(message)


# Нормализует веса в состоянии по принципу нормализации вектора
def normalize_state(st):
    max_weight = 0
    for key in st['weights'].keys():
        max_weight = max(max_weight, st['weights'][key])
    if max_weight == 0:
        return
    for key in st['weights'].keys():
        st['weights'][key] /= max_weight


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
# -update <session_id> <question_id> <ratio> применить влияние вопроса на результат с коэф. ratio
#   (см. функцию apply_question_to_state)
# -get_question <session_id> <strictness>(опционально) вернуть подходящий пользователю вопрос.
#   Рандомность определяется параметром strictness (0-рандом, 1-строго). См документацию в файле question_chooser.py
#
# TODO -delete <session_id> удалить сессию
# TODO -new <session_id> создать сессию
if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == '-update':
        session_id = int(sys.argv[2])
        question_id = int(sys.argv[3])
        ratio = int(sys.argv[4])

        state = (import_state(session_id))
        question = (import_question_data(question_id))

        apply_question_to_state(question, state, ratio)
        normalize_state(state)

        write_state(session_id, state)
    elif arg == '-get_question':
        session_id = int(sys.argv[2])
        state = import_state(session_id)

        if len(sys.argv) > 3:
            strictness = int(sys.argv[3])
            emit(choose_relevant(state, strictness=strictness))
        else:
            emit(choose_relevant(state))
    else:
        print('Ошибка: неизвестный аргумент')
