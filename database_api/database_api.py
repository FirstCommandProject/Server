import mysql.connector
import json

database = mysql.connector.connect(
        host="188.225.24.248",
        user="root",
        password="dynamicSystem2a",
        database="ExpertSystem",
        auth_plugin='mysql_native_password'
    )


#
# Функция нужна для выполнения запросов, которые не были предусмотрены. (Расширение кода).
#
def make_custom_request(tag, massive):
    try:
        cursor = database.cursor(prepared=True)
        request = f"SELECT * FROM ExpertSystem.Questions WHERE " \
            f'JSON_CONTAINS(tags,\'["{tag}"]\') AND id NOT IN ("{massive}") ORDER BY RAND() LIMIT 1'
        cursor.execute(request)

        result = cursor.fetchall()
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


#
# Функция выполняет авторизацию пользователя. Пароль должен поставляться в хеш. формате.
#
def authorize_user(login, password):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT 1 FROM ExpertSystem.Users WHERE login = %s AND password = %s", (login, password,))

        result = cursor.fetchall()
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


#
# Функция добавляет нового пользователя в БД.
#
def add_new_user(login, password, name, surname, patronymic, university):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"INSERT INTO ExpertSystem.Users VALUES(%s, %s, %s, %s, %s, %s)", (login, password, name, surname, patronymic, university,))

        result = [0]
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


def insert_table_results(login, weights, time):
    try:
        cursor = database.cursor()
        cursor.execute(f"INSERT INTO Results VALUES('{login}', '{weights}', '{time}')")

        result = [0]
        database.commit()

        return result
    except mysql.connector.ProgrammingError as error:
        return error.errno


#
# Функция обновляет данные пользователя в БД.
#
def update_user_data(old_login, new_login, new_password, new_name, new_surname, new_patronymic, new_university):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"UPDATE ExpertSystem.Users SET login = %s, password = %s, name = %s, surname = %s, patronymic "
                       f"= %s, university = %s WHERE login = %s", (new_login, new_password, new_name, new_surname,
                                                                   new_patronymic, new_university, old_login,))

        result = [0]
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


def restore_user_password(login, password):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"UPDATE ExpertSystem.Users SET password = %s WHERE login = %s", (password, login,))

        result = [0]
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


def select_user_data(login):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT login, name, surname, patronymic, university FROM ExpertSystem.Users WHERE login = %s",
                       (login,))

        result = cursor.fetchall()
        dictionary = {'email': result[0][0], 'firstName': result[0][1], 'secondName': result[0][2], 'university': result[0][3]}
        database.commit()

        return dictionary
    except mysql.connector.Error as error:
        return error.errno


#
# Функция возвращает данные вопроса по его айди.
#
def select_question_by_id(question_id):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT * FROM ExpertSystem.Questions WHERE id = %s", (question_id,))

        result = cursor.fetchall()
        dictionary = {'id': int(result[0][0]), 'title': result[0][1], 'tags': list(result[0][2]), 'weights': json.loads(result[0][3])}

        database.commit()

        return dictionary
    except mysql.connector.Error as error:
        return error.errno


#
# Функция возвращает последний результат из БД по логину.
#
def select_last_result(user_login):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT * FROM ExpertSystem.Results WHERE login = %s ORDER BY time DESC LIMIT 1", (user_login,))

        result = cursor.fetchall()
        dictionary = {}
        dictionary.update({'login':result[0], 'session':result[1], 'time':result[2]})
        database.commit()

        return dictionary
    except mysql.connector.Error as error:
        return error.errno


#
# Функция возвращает определенное кол-во результатов пользователя.
#
def select_user_results(user_login, limit, offset):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT * FROM ExpertSystem.Results WHERE login = %s ORDER BY time DESC LIMIT %s OFFSET %s",
                       (user_login, limit, offset))

        result = cursor.fetchall()
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


#
# Функция возвращает определенный результат по времени.
#
def select_user_result_by_time(user_login, question_time):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT * FROM ExpertSystem.Results WHERE login = %s AND time = %s", (user_login, question_time))

        result = cursor.fetchall()
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


#
# Функция возвращает кол-во всех кафедр в БД.
#
def select_cafedras_count():
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT Count(*) FROM ExpertSystem.Cafedras")

        result = cursor.fetchall()
        database.commit()

        return result
    except mysql.connector.Error as error:
        return error.errno


#
# Функция получает все данные о кафедре по ID.
#
def select_cafedra_by_id(cafedra_id):
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute(f"SELECT * FROM ExpertSystem.Cafedras WHERE id = %s", (cafedra_id,))
        result = cursor.fetchall()
        dictionary = {'id': result[0], 'name': result[1], 'description': result[2], 'price': result[3], 'years': result[4], 'form': result[5]}
        database.commit()

        return dictionary
    except mysql.connector.Error as error:
        return error.errno


#
# Функция получает все данные об определенных кафедрах.
#
def select_cafedras():
    try:
        cursor = database.cursor(prepared=True)
        cursor.execute("SELECT * FROM Cafedras")
        list1 = []
        dictionary = {}
        result = cursor.fetchall()
        for i in range(len(result)):
            dictionary.update({'id': result[i][0], 'name': result[i][1], 'description': result[i][2], 'price': result[i][3], 'years': result[i][4], 'form': result[i][5]})
            list1.append(dictionary)
            dictionary = {}
        result_dictionary = {}
        result_dictionary.update(
            statusCode='200',
            data=list1
        )

        database.commit()
        return result_dictionary
    except mysql.connector.Error as error:
        return error.errno


# Tests

# print(make_custom_request(f"UPDATE ExpertSystem.Users SET name = %s WHERE login = %s", ("123123123 me", "ab")))
# print(make_custom_request(f"SELECT * FROM ExpertSystem.Users WHERE login = %s AND password = %s", "login", "password"))
# print(authorize_user("login", "password"))
# print(add_new_user("a", "a", "a", "a", "a", "a"))
# print(update_user_data("a", "ab", "a", "a", "a", "a", "a"))
# print(select_user_data("login"))
# print(select_question_by_id(1))
# print(select_user_results("login", 1, 0))
# print(select_cafedras_count())
# print(select_cafedra_by_id(1))
# print(select_cafedras(1, 0))
#print(select_user_data('d_savosin@list.ru'))
#select_cafedras()
#print(select_question_by_id(3))
#print(make_custom_request('["chemistry"]', "1, 2, 3, 4, 5"))
#print(make_custom_request("math", "1, 2, 3"))
#print(make_custom_request())
#print(select_question_by_id(3))
#print(select_cafedras())
