import random
from database_api.database_api import *

DEBUG: bool = True


def debug_print(*args):
    if DEBUG:
        print(*args)


# Нормализует веса в состоянии по принципу нормализации вектора
def _normalize_user_weights(st):
    max_weight = 0
    for key in st['weights'].keys():
        max_weight = max(max_weight, st['weights'][key])
    if max_weight == 0:
        return
    for key in st['weights'].keys():
        st['weights'][key] /= max_weight


def _update_answered_list(user_session_data, question_id):
    user_session_data['answered'].append(question_id)
    debug_print(f" -- Answered list updated with {question_id}. answered={user_session_data['answered']}")


def _choose_random_question_by_tag(user_session_data, relevant_tag):
    raw_array_representation = ''  # Example: 2, 6, 10, 11
    for answered_id in user_session_data['answered']:
        if raw_array_representation != '':
            raw_array_representation += ', '
        raw_array_representation += (str(answered_id))
    debug_print(f" -- Answered array string representation: {raw_array_representation}")
    query = f"SELECT * FROM ExpertSystem.Questions WHERE " \
            f"JSON_CONTAINS(tags, '[{relevant_tag}]') AND id NOT IN ({raw_array_representation}) ORDER BY RAND() LIMIT 1"
    random_question = make_custom_request(relevant_tag, raw_array_representation)
    return random_question


# Выбирает актуальный тег для пользователя, основываясь на уже известных предпочтениях
# Поиск производится по тегам, указанным в вопросах
# Выбирается один из тегов, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает тег
def _choose_relevant_tag(user_session_data, strictness, excluded_tags) -> str:
    try:
        assert user_session_data['weights']
        assert 0 <= strictness <= 1
    except AssertionError:
        return None

    tags = list(user_session_data['weights'].keys())
    for to_exclude in excluded_tags:
        if to_exclude in tags:
            tags.remove(to_exclude)
    chosen_tag_index = random.randint(0, len(tags) - 1)
    change = random.random() / (1 + strictness) > \
             (user_session_data['weights'][tags[chosen_tag_index]] * strictness) and strictness != 0
    while change:
        change = random.random() / (1 + strictness) > (
                    user_session_data['weights'][tags[chosen_tag_index]] * strictness)
        chosen_tag_index = random.randint(0, len(tags) - 1)
    return tags[chosen_tag_index]


# Выбирает актуальный вопрос для пользователя, основываясь на уже известных предпочтениях
# Поиск производится по тегам, указанным в вопросах
# Выбирается один из вопрос, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает вопрос в виде json
def choose_relevant_question(user_session_data, strictness=0.75) -> dict:
    debug_print(f"Choose relevant question call: session={user_session_data}")
    try:
        relevant_question = []
        excluded_tags = []
        while not relevant_question:
            relevant_tag = _choose_relevant_tag(user_session_data, strictness=strictness, excluded_tags=excluded_tags)
            excluded_tags.append(relevant_tag)
            debug_print(f" -- Relevant tag chosen: {relevant_tag}")
            relevant_question = _choose_random_question_by_tag(user_session_data, relevant_tag)
            debug_print(f" -- Relevant question chosen: {relevant_question}")

        assert relevant_question != []
        res_dict = {'id': relevant_question[0][0], 'title': relevant_question[0][1],
                'tags': relevant_question[0][2],
                'weights': relevant_question[0][3]}
        debug_print(f" -- Relevant question successfully built!")
        return res_dict
    except Exception as e:
        print(f"Exception! {str(e)}")
        return None


# Ratio 1 - полностью применить. Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 2
# Ratio 0.5 - частично применить.Пример:Математика: 1,в вопросе математика: 2,в итоге в состоянии будет математика: 1.5
# Ratio 0 - ничего не применять
# Ratio -0.5 - частично применить в обратную сторону.
# Ratio -1 - применить в обратную сторону.
#   Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 0.5
def update_weights(user_session_data, question_id, ratio) -> dict:
    debug_print(f"Update weights call: id={question_id}, ratio: {ratio}")
    if ratio == 0:
        return user_session_data
    question: dict = select_question_by_id(question_id)  # Вызов API для получения нужного вопроса
    debug_print(f" -- Got question: {question}")
    question_keys = question['weights'].keys()

    for key in question_keys:
        if user_session_data['weights'].get(key):
            if ratio == 1:
                user_session_data['weights'][key] *= question['weights'][key]
            elif ratio == 0.5:
                user_session_data['weights'][key] *= (question['weights'][key] + 1) / 2
            elif ratio == -0.5:
                user_session_data['weights'][key] /= (question['weights'][key] + 1) / 2
            elif ratio == -1:
                user_session_data['weights'][key] /= question['weights'][key]
            else:
                # Unsupported ratio
                return None
    debug_print(f" -- Weights updated!")
    _update_answered_list(user_session_data, question_id)
    _normalize_user_weights(user_session_data)
    return user_session_data


# Считает очки кафедры для конкретного человека по его результатам
def _calculate_cafedra_score(user_session_data, cafedra_data) -> int:

    score = 0

    user_disciplines = set(user_session_data.keys())
    cafedra_disciplines = set(cafedra_data['weights'].keys())
    common_disciplines = user_disciplines & cafedra_disciplines

    for disc in common_disciplines:
        score += user_session_data[disc] * cafedra_data['weights'][disc]

    return score


def calculate_cafedras_score(user_session_data) -> list:
    raw = tuple()
    cafedras = select_cafedras()['data']
    for c in cafedras:
        raw += (_calculate_cafedra_score(user_session_data, c), c['id'])
    raw = sorted(raw)
    result = []
    for d in raw:
        result.append({'id': d[1], 'score': d[0]})
    return result
