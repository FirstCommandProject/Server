import mysql.connector


# Функция, которая проверяет на наличие sql запроса DROP TABLE
def _find_injection(string):
    string = str(string)
    if "DROP TABLE" in string or "--" in string or ";" in string:
        return 1
    else:
        return 0


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу id
def select_table_questions_id(id):
    cursor = database.cursor()
    if _find_injection(id) == 0:
        cursor.execute(f"SELECT * FROM Questions WHERE id = '{id}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу text
def select_table_questions_text(text):
    cursor = database.cursor()
    if _find_injection(text) == 0:
        cursor.execute(f"SELECT * FROM Questions WHERE text = '{text}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу tags
def select_table_questions_tags(tags):
    cursor = database.cursor()
    if _find_injection(tags) == 0:
        cursor.execute(f"SELECT * FROM Questions WHERE JSON_CONTAINS(tags, '[{tags}]')")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу weights
def select_table_questions_weights():
    cursor = database.cursor()
    cursor.execute(f"SELECT weights FROM Questions")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Questions по всем столбцам
def select_table_questions_all_rows():
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Questions")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу login
def select_table_users_login(login):
    cursor = database.cursor()
    if _find_injection(login) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE login = '{login}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по столбцу password
def select_table_users_password(password):
    cursor = database.cursor()
    if _find_injection(password) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE password = '{password}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по столбцу name
def select_table_users_name(name):
    cursor = database.cursor()
    if _find_injection(name) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE name = '{name}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по столбцу surname
def select_table_users_surname(surname):
    cursor = database.cursor()
    if _find_injection(surname) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE surname = '{surname}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по столбцу patronymic
def select_table_users_patronymic(patronymic):
    cursor = database.cursor()
    if _find_injection(patronymic) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE patronymic = '{patronymic}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по столбцу university
def select_table_users_university(university):
    cursor = database.cursor()
    if _find_injection(university) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE university = '{university}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Users по всем столбцам
def select_table_users_all_rows():
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Results по столбцу login
def select_table_results_login(login):
    cursor = database.cursor()
    if _find_injection(login) == 0:
        cursor.execute(f"SELECT * FROM Users WHERE login = '{login}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result


# Функция, которая выполняет sql запрос select к таблице Results по столбцу weights
def select_table_results_weights():
    cursor = database.cursor()
    cursor.execute(f"SELECT weights FROM Results")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Results по столбцу time
def select_table_results_login(time):
    cursor = database.cursor()
    if _find_injection(time) == 0:
        cursor.execute(f"SELECT * FROM Results WHERE time = '{time}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Results по всем столбцам
def select_table_results_all_rows():
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Results")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу id
def select_table_cafedras_id(id):
    cursor = database.cursor()
    if _find_injection(id) == 0:
        cursor.execute(f"SELECT * FROM Cafedras WHERE id = '{id}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу title
def select_table_cafedras_title(title):
    cursor = database.cursor()
    if _find_injection(title) == 0:
        cursor.execute(f"SELECT * FROM Cafedras WHERE title = '{title}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу university
def select_table_cafedras_university(university):
    cursor = database.cursor()
    if _find_injection(university) == 0:
        cursor.execute(f"SELECT * FROM Cafedras WHERE university = '{university}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу firstData
def select_table_cafedras_firstData(firstData):
    cursor = database.cursor()
    if _find_injection(firstData) == 0:
        cursor.execute(f"SELECT * FROM Cafedras WHERE firstData = '{firstData}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу secondData
def select_table_cafedras_secondData(secondData):
    cursor = database.cursor()
    if _find_injection(secondData) == 0:
        cursor.execute(f"SELECT * FROM Cafedras WHERE secondData = '{secondData}'")
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result
    else:
        print("Error")


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу weights
def select_table_cafedras_weights():
    cursor = database.cursor()
    cursor.execute(f"SELECT weights FROM Cafedras")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по всем столбцам
def select_table_cafedras_all_rows():
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Cafedras")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос insert к таблице Results
def insert_table_results(login, weights, time):
    cursor = database.cursor()
    if _find_injection(login) == 0 and _find_injection(weights) == 0 and _find_injection(time) == 0:
        cursor.execute(f"INSERT INTO Results VALUES('{login}', '{weights}', '{time}')")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу login
def upsert_table_users_login(last_login, new_login):
    cursor = database.cursor()
    if _find_injection(last_login) == 0 and _find_injection(new_login) == 0:
        cursor.execute(f"UPDATE Users SET login = '{new_login}' WHERE login = '{last_login}'")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу password
def upsert_table_users_password(login, new_password):
    cursor = database.cursor()
    if _find_injection(new_password) == 0 and _find_injection(login) == 0:
        cursor.execute(f"UPDATE Users SET password = '{new_password}' WHERE login = '{login}'")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу name
def upsert_table_users_name(login, new_name):
    cursor = database.cursor()
    if _find_injection(login) == 0 and _find_injection(new_name) == 0:
        cursor.execute(f"UPDATE Users SET name = '{new_name}' WHERE login = '{login}'")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу surname
def upsert_table_users_surname(login, new_surname):
    cursor = database.cursor()
    if _find_injection(login) == 0 and _find_injection(new_surname) == 0:
        cursor.execute(f"UPDATE Users SET surname = '{new_surname}' WHERE login = '{login}'")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу patronymic
def upsert_table_users_patronymic(login, new_patronymic):
    cursor = database.cursor()
    if _find_injection(login) == 0 and _find_injection(new_patronymic) == 0:
        cursor.execute(f"UPDATE Users SET patronymic = '{new_patronymic}' WHERE login = '{login}'")
        database.commit()
    else:
        print("Error")


# Функция, которая выполняет sql запрос update к таблице Users по столбцу university
def upsert_table_users_university(login, new_university):
    cursor = database.cursor()
    if _find_injection(login) == 0 and _find_injection(new_university) == 0:
        cursor.execute(f"UPDATE Users SET university = '{new_university}' WHERE login = '{login}'")
        database.commit()
    else:
        print("Error")


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
