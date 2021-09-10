import random
import Server.database_api.database_api as database_api


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
    assert user_session_data['answered']
    user_session_data['answered'].append(question_id)


def _choose_random_question_by_tag(user_session_data, relevant_tag):
    raw_array_representation = ''  # Example: 2, 6, 10, 11
    for answered_id in user_session_data['answered']:
        if raw_array_representation != '':
            raw_array_representation.append(', ')
        raw_array_representation.append(str(answered_id))

    query = f"SELECT * FROM ExpertSystem.Questions WHERE " \
            f"JSON_CONTAINS(tags, '[{relevant_tag}]') AND id NOT IN ({raw_array_representation}) ORDER BY RAND() LIMIT 1"

    random_question = database_api.make_custom_request(query)
    return random_question


# Выбирает актуальный тег для пользователя, основываясь на уже известных предпочтениях
# Поиск производится по тегам, указанным в вопросах
# Выбирается один из тегов, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает тег
def _choose_relevant_tag(user_session_data, strictness) -> str:
    try:
        assert user_session_data['weights']
        assert 0 <= strictness <= 1
    except AssertionError:
        return None

    tags = list(user_session_data['weights'].keys())
    chosen_tag_index = random.randint(0, len(tags) - 1)
    change = random.random() / (1 + strictness) > \
             (user_session_data['weights'][tags[chosen_tag_index]] * strictness) and strictness != 0
    while change:
        change = random.random() / (1 + strictness) > (
                    user_session_data['weights'][tags[chosen_tag_index]] * strictness)
        chosen_tag_index = random.randint(0, len(tags) - 1)
    return tags[chosen_tag_index]


# Выбирает актуальный вопрос для пользователя, основываясь на уже известных предпочтениях
# Возвращает id
def _choose_relevant_question_id(user_session_data, strictness) -> int:
    try:
        relevant_tag = _choose_relevant_tag(user_session_data, strictness=strictness)
        relevant_question_id = _choose_random_question_by_tag(user_session_data, relevant_tag)['id']
        return relevant_question_id
    except:
        return -1


# Выбирает актуальный вопрос для пользователя, основываясь на уже известных предпочтениях
# Поиск производится по тегам, указанным в вопросах
# Выбирается один из вопрос, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает вопрос в виде json
def choose_relevant_question(user_session_data, strictness=0.75) -> dict:
    try:
        relevant_tag = _choose_relevant_tag(user_session_data, strictness=strictness)
        relevant_question = _choose_random_question_by_tag(user_session_data, relevant_tag)
        return relevant_question
    except:
        return None


# Ratio 1 - полностью применить. Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 2
# Ratio 0.5 - частично применить.Пример:Математика: 1,в вопросе математика: 2,в итоге в состоянии будет математика: 1.5
# Ratio 0 - ничего не применять
# Ratio -0.5 - частично применить в обратную сторону.
# Ratio -1 - применить в обратную сторону.
#   Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 0.5
def update_weights(user_session_data, question_id, ratio) -> dict:
    try:
        assert user_session_data['answered']
        assert user_session_data['weights']

        if ratio == 0:
            return user_session_data

        question: dict = database_api.select_question_by_id(question_id)  # Вызов API для получения нужного вопроса
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

        _update_answered_list(user_session_data, question_id)
        _normalize_user_weights(user_session_data)
    except:
        return None

    return user_session_data
