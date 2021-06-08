import random
import database_api


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


# Выбирает актуальный тег для пользователя, основываясь на уже известных предпочтениях
# Поиск производится по тегам, указанным в вопросах
# Выбирается один из тегов, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает тег
def choose_relevant_tag(user_session_data, strictness=0.75) -> str:
    try:
        assert user_session_data['weights']
        assert 0 <= strictness <= 1
    except AssertionError:
        return None

    tags = list(user_session_data['weights'].keys())
    chosen_tag_index = random.randint(0, len(tags)-1)
    change = random.random()/(1+strictness) > \
             (user_session_data['weights'][tags[chosen_tag_index]] * strictness) and strictness != 0
    while change:
        change = random.random()/(1+strictness) > (user_session_data['weights'][tags[chosen_tag_index]] * strictness)
        chosen_tag_index = random.randint(0, len(tags)-1)
    return tags[chosen_tag_index]


# Ratio 1 - полностью применить. Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 2
# Ratio 0.5 - частично применить.Пример:Математика: 1,в вопросе математика: 2,в итоге в состоянии будет математика: 1.5
# Ratio 0 - ничего не применять
# Ratio 0.5 - частично применить в обратную сторону.
# Ratio -1 - применить в обратную сторону.
#   Пример: Математика: 1, в вопросе математика: 2, в итоге в состоянии будет математика: 0.5
def update_weights(user_session_data, question_id, ratio) -> dict:
    try:
        assert user_session_data['answered']
        assert user_session_data['weights']
    except AssertionError:
        return None

    if ratio == 0:
        return user_session_data

    question: dict = database_api.get_question(question_id)  # Вызов API для получения нужного вопроса
    question_keys = question['weights'].keys()

    for key in question_keys:
        if user_session_data['weights'].get(key):
            if ratio == 1:
                user_session_data['weights'][key] *= question['weights'][key]
            elif ratio == 0.5:
                user_session_data['weights'][key] *= (question['weights'][key] + 1)/2
            elif ratio == -0.5:
                user_session_data['weights'][key] /= (question['weights'][key] + 1)/2
            elif ratio == -1:
                user_session_data['weights'][key] /= question['weights'][key]
            else:
                # Unsupported ratio
                return None

    _update_answered_list(user_session_data, question_id)
    _normalize_user_weights(user_session_data)

    return user_session_data
