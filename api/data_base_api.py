import mysql.connector


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу id
def select_table_questions_id(id):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Questions WHERE id = %s", (int(id), ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу text
def select_table_questions_text(text):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Questions WHERE text = %s", (text, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу tags
def select_table_questions_tags(tags):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Questions WHERE JSON_CONTAINS(tags, '[{tags}]')")
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


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
    cursor.execute(f"SELECT * FROM Users WHERE login = %s", (login, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу password
def select_table_users_password(password):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE password = %s", (password, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу name
def select_table_users_name(name):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE name = %s", (name, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу surname
def select_table_users_surname(surname):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE surname = %s", (surname, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу patronymic
def select_table_users_patronymic(patronymic):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE patronymic = %s", (patronymic, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Users по столбцу university
def select_table_users_university(university):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE university = %s", (university, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


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
    cursor.execute(f"SELECT * FROM Users WHERE login = %s", (login, ))
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
def select_table_results_time(time):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Results WHERE time = %s", (time, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


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
    cursor.execute(f"SELECT * FROM Cafedras WHERE id = %s", (int(id), ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу title
def select_table_cafedras_title(title):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Cafedras WHERE title = %s", (title, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу university
def select_table_cafedras_university(university):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Cafedras WHERE university = %s", (university, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу firstData
def select_table_cafedras_firstData(firstData):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Cafedras WHERE firstData = %s", (firstData, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу secondData
def select_table_cafedras_secondData(secondData):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM Cafedras WHERE secondData = %s", (secondData, ))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        return result


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
    cursor.execute(f"INSERT INTO Results VALUES('{login}', '{weights}', '{time}')")
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу login
def upsert_table_users_login(last_login, new_login):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET login = %s WHERE login = %s", (last_login, new_login, ))
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу password
def upsert_table_users_password(login, new_password):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET password = %s WHERE login = %s", (new_password, login, ))
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу name
def upsert_table_users_name(login, new_name):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET name = %s WHERE login = %s", (new_name, login, ))
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу surname
def upsert_table_users_surname(login, new_surname):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET surname = %s WHERE login = %s", (new_surname, login, ))
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу patronymic
def upsert_table_users_patronymic(login, new_patronymic):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET patronymic = %s WHERE login = %s", (new_patronymic, login, ))
    database.commit()


# Функция, которая выполняет sql запрос update к таблице Users по столбцу university
def upsert_table_users_university(login, new_university):
    cursor = database.cursor()
    cursor.execute(f"UPDATE Users SET university = %s WHERE login =  %s", (new_university, login, ))
    database.commit()


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
