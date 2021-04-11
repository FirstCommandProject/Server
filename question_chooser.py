import random
from Server.file_io import get_questions_list, import_question_data


# Выбирает актуальный вопрос для пользователя, основываясь на уже известных предпочтениях
# Хотя скорее всего выберется вопрос по наиболее интересной теме, остается шанс на вопрос по неинтересной теме,
# для большей гибкости.
# Поиск производится по тегам, указанным в вопросах
# Алгоритм: 1. Выбирается один из тегов, который, вероятно, интересен человеку (хотя иногда может быть неинтересен)
#           2. Выбирается случайный вопрос с нужным тегом
# Пармаетр strictness означает насколько строго будет выбираться (0 - рандомно, 1 - максимально строго)
# Крайне не рекомендуется выбирать значения strictness в пределах от 0.000...1 до 0.2
# Возвращает ID выбранного вопроса
def choose_relevant(state, strictness=0.75) -> int:
    questions_id = get_questions_list()

    assert state['weights']

    # 1.
    tags = list(state['weights'].keys())
    chosen_tag_index = random.randint(0, len(tags)-1)
    change = random.random()/(1+strictness) > \
             (state['weights'][tags[chosen_tag_index]] * strictness) and strictness != 0
    while change:
        change = random.random()/(1+strictness) > (state['weights'][tags[chosen_tag_index]] * strictness)
        chosen_tag_index = random.randint(0, len(tags)-1)

    # 2.
    potential_questions = []
    for qid in questions_id:
        q = import_question_data(qid)
        if tags[chosen_tag_index] in q['tags']:
            potential_questions.append(qid)

    # Непредвиденная ситуация (если нет вопросов с таким тегом)
    if len(potential_questions) == 0:
        print(f"Warning: no questions with tag '{tags[chosen_tag_index]}'")
        return choose_relevant(state, strictness/2)

    return potential_questions[random.randint(0, len(potential_questions)-1)]

