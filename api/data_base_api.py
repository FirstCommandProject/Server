import mysql.connector
import unittest
import datetime
# !/usr/bin/python
# -*- coding: utf8 -*-

# Функция, которая выполняет sql запрос select к таблице Questions по столбцу id
def select_table_questions_id(id):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Questions WHERE id = %s", (int(id),))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу text
def select_table_questions_text(text):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Questions WHERE text = %s", (text,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result

    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу tags
def select_table_questions_tags(tags):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Questions WHERE JSON_CONTAINS(tags, '[{tags}]')")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу weights
def select_table_questions_weights():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT weights FROM Questions")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Questions по всем столбцам
def select_table_questions_all_rows():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Questions")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу login
def select_table_users_login(login):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE login = %s", (login,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу password
def select_table_users_password(password):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE password = %s", (password,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу name
def select_table_users_name(name):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE name = %s", (name,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу surname
def select_table_users_surname(surname):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE surname = %s", (surname,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу patronymic
def select_table_users_patronymic(patronymic):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE patronymic = %s", (patronymic,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по столбцу university
def select_table_users_university(university):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE university = %s", (university,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Users по всем столбцам
def select_table_users_all_rows():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Users")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Results по столбцу login
def select_table_results_login(login):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Results WHERE login = %s", (login,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Results по столбцу weights
def select_table_results_weights():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT weights FROM Results")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Results по столбцу time
def select_table_results_time(time):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Results WHERE time = %s", (time,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Results по всем столбцам
def select_table_results_all_rows():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Results")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу id
def select_table_cafedras_id(id):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras WHERE id = %s", (int(id),))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу title
def select_table_cafedras_title(title):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras WHERE title = %s", (title,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу university
def select_table_cafedras_university(university):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras WHERE university = %s", (university,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу firstData
def select_table_cafedras_firstData(firstData):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras WHERE firstData = %s", (firstData,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу secondData
def select_table_cafedras_secondData(secondData):
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras WHERE secondData = %s", (secondData,))
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по столбцу weights
def select_table_cafedras_weights():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT weights FROM Cafedras")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос select к таблице Cafedras по всем столбцам
def select_table_cafedras_all_rows():
    try:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM Cafedras")
        result = cursor.fetchall()
        result.insert(0, 0)
        return result
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос insert к таблице Results
def insert_table_results(login, weights, time):
    try:
        cursor = database.cursor()
        cursor.execute(f"INSERT INTO Results VALUES('{login}', '{weights}', '{time}')")
        database.commit()
    except mysql.connector.ProgrammingError as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу login
def upsert_table_users_login(last_login, new_login):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET login = %s WHERE login = %s", (last_login, new_login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу password
def upsert_table_users_password(login, new_password):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET password = %s WHERE login = %s", (new_password, login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу name
def upsert_table_users_name(login, new_name):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET name = %s WHERE login = %s", (new_name, login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу surname
def upsert_table_users_surname(login, new_surname):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET surname = %s WHERE login = %s", (new_surname, login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу patronymic
def upsert_table_users_patronymic(login, new_patronymic):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET patronymic = %s WHERE login = %s", (new_patronymic, login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Функция, которая выполняет sql запрос update к таблице Users по столбцу university
def upsert_table_users_university(login, new_university):
    try:
        cursor = database.cursor()
        cursor.execute(f"UPDATE Users SET university = %s WHERE login =  %s", (new_university, login,))
        database.commit()
    except mysql.connector.Error as err:
        return err.errno


# Провожу Unit тестирование каждой функции
class api_test(unittest.TestCase):
    def test_select_table_questions_id_1(self):
        self.assertEqual(select_table_questions_id(1), [0, (1, 'Вы любите космические исследования?', '["math", "astronomy", "programming"]', '{"math": 1.5, "anatomy": 0.4, "biology": 0.4, "economy": 0.9, "business": 1, "astronomy": 1.3, "chemistry": 0.6, "geography": 1.2, "psyhology": 0.8, "engineering": 1.4, "informatics": 1.6, "linguistics": 0.6, "programming": 1.2, "political science": 0.3, "religious studies": 0.2}')])

    def test_select_table_questions_id_2(self):
        self.assertEqual(select_table_questions_id(8), [0])

    def test_select_table_questions_text_1(self):
        self.assertEqual(select_table_questions_text("Вам нравятся гуманитарные предметы?"), [0, (2, 'Вам нравятся гуманитарные предметы?', '["psyhology", "linguistics", "biology", "anatomy", "religious studies", "political science", "chemistry", "business"]', '{"math": 0.5, "anatomy": 1.5, "biology": 1.5, "economy": 0.5, "business": 0.5, "astronomy": 0.5, "chemistry": 1.5, "geography": 1.5, "psyhology": 1.5, "engineering": 0.5, "informatics": 0.5, "linguistics": 1.5, "programming": 0.5, "political science": 1.5, "religious studies": 1.5}')])

    def test_select_table_questions_text_2(self):
        self.assertEqual(select_table_questions_text("Вам нравятся машины?"), [0])

    def test_select_table_questions_tags_1(self):
        self.assertEqual(select_table_questions_tags('"math", "astronomy", "programming"'), [0, (1, 'Вы любите космические исследования?', '["math", "astronomy", "programming"]', '{"math": 1.5, "anatomy": 0.4, "biology": 0.4, "economy": 0.9, "business": 1, "astronomy": 1.3, "chemistry": 0.6, "geography": 1.2, "psyhology": 0.8, "engineering": 1.4, "informatics": 1.6, "linguistics": 0.6, "programming": 1.2, "political science": 0.3, "religious studies": 0.2}')])

    def test_select_table_questions_tags_2(self):
        self.assertEqual(select_table_questions_tags("math"), 3141)

    def test_select_table_questions_tags_3(self):
        self.assertEqual(select_table_questions_tags('"math"'), [0, (1, 'Вы любите космические исследования?', '["math", "astronomy", "programming"]', '{"math": 1.5, "anatomy": 0.4, "biology": 0.4, "economy": 0.9, "business": 1, "astronomy": 1.3, "chemistry": 0.6, "geography": 1.2, "psyhology": 0.8, "engineering": 1.4, "informatics": 1.6, "linguistics": 0.6, "programming": 1.2, "political science": 0.3, "religious studies": 0.2}'), (3, 'Вам нравится теоретическая информатика?', '["math", "informatics", "programming", "engineering"]', '{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 1.1, "astronomy": 1.2, "chemistry": 0.5, "geography": 0.5, "psyhology": 0.7, "engineering": 1.25, "informatics": 1.6, "linguistics": 0.5, "programming": 1.4, "political science": 0.5, "religious studies": 0.5}'), (4, 'Вам нравится экономика?', '["math", "economy", "linguistics", "geography"]', '{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 1.7, "business": 1.2, "astronomy": 1.2, "chemistry": 0.5, "geography": 1.2, "psyhology": 0.6, "engineering": 0.5, "informatics": 1.3, "linguistics": 0.6, "programming": 1.3, "political science": 1.5, "religious studies": 0.5}')])

    def test_select_table_questions_weigths(self):
        self.assertEqual(select_table_questions_weights(), [0, ('{"math": 1.5, "anatomy": 0.4, "biology": 0.4, "economy": 0.9, "business": 1, "astronomy": 1.3, "chemistry": 0.6, "geography": 1.2, "psyhology": 0.8, "engineering": 1.4, "informatics": 1.6, "linguistics": 0.6, "programming": 1.2, "political science": 0.3, "religious studies": 0.2}',), ('{"math": 0.5, "anatomy": 1.5, "biology": 1.5, "economy": 0.5, "business": 0.5, "astronomy": 0.5, "chemistry": 1.5, "geography": 1.5, "psyhology": 1.5, "engineering": 0.5, "informatics": 0.5, "linguistics": 1.5, "programming": 0.5, "political science": 1.5, "religious studies": 1.5}',), ('{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 1.1, "astronomy": 1.2, "chemistry": 0.5, "geography": 0.5, "psyhology": 0.7, "engineering": 1.25, "informatics": 1.6, "linguistics": 0.5, "programming": 1.4, "political science": 0.5, "religious studies": 0.5}',), ('{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 1.7, "business": 1.2, "astronomy": 1.2, "chemistry": 0.5, "geography": 1.2, "psyhology": 0.6, "engineering": 0.5, "informatics": 1.3, "linguistics": 0.6, "programming": 1.3, "political science": 1.5, "religious studies": 0.5}',)])

    def test_select_table_users_login_1(self):
        self.assertEqual(select_table_users_login("zerg12345"), [0, ('zerg12345', 'PUTIN', 'KOLYA', 'SVECHNIKAR', 'keraj', 'KUBGAU')])

    def test_select_table_users_login_2(self):
        self.assertEqual(select_table_users_login("DIMA123456789"), [0])

    def test_select_table_users_password_1(self):
        self.assertEqual(select_table_users_password("GG"), [0, ('kukuha', 'GG', 'Sasha', 'Kostylev', 'Valerevich', 'ITMO')])

    def test_select_table_users_password_2(self):
        self.assertEqual(select_table_users_password("PYTRPYRTY"), [0])

    def test_select_table_users_name_1(self):
        self.assertEqual(select_table_users_name("Dima"), [0])

    def test_select_table_users_name_2(self):
        self.assertEqual(select_table_users_name("KOLYA"), [0, ('zerg12345', 'PUTIN', 'KOLYA', 'SVECHNIKAR', 'keraj', 'KUBGAU')])

    def test_select_table_users_surname_1(self):
        self.assertEqual(select_table_users_surname("SVECHNIKAR"), [0, ('zerg12345', 'PUTIN', 'KOLYA', 'SVECHNIKAR', 'keraj', 'KUBGAU')])

    def test_select_table_users_surname_2(self):
        self.assertEqual(select_table_users_surname("GUGUGUGUG"), [0])

    def test_select_table_users_patronymic_1(self):
        self.assertEqual(select_table_users_patronymic("Valerevich"), [0, ('kukuha', 'GG', 'Sasha', 'Kostylev', 'Valerevich', 'ITMO')])

    def test_select_table_users_patronymic_2(self):
        self.assertEqual(select_table_users_patronymic("jdajsajdjasd"), [0])

    def test_select_table_users_university_1(self):
        self.assertEqual(select_table_users_university("ITMO"), [0, ('kukuha', 'GG', 'Sasha', 'Kostylev', 'Valerevich', 'ITMO')])

    def test_select_table_users_university_2(self):
        self.assertEqual(select_table_users_university("eqeqweqweq"), [0])

    def test_select_table_results_login_1(self):
        self.assertEqual(select_table_results_login("kerer"), [0, ('kerer', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}', datetime.datetime(2015, 5, 7, 10, 5, 23))])

    def test_select_table_results_login_2(self):
        self.assertEqual(select_table_results_login("adsadas"), [0])

    def test_select_table_results_time_1(self):
        self.assertEqual(select_table_results_time(datetime.datetime(2015, 5, 7, 10, 5, 23)), [0, ('kerer', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}', datetime.datetime(2015, 5, 7, 10, 5, 23))])

    def test_select_table_results_time_2(self):
        self.assertEqual(select_table_results_time("2015"), 1525)

    def test_select_table_cafedras_id_1(self):
        self.assertEqual(select_table_cafedras_id(1), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])

    def test_select_table_cafedras_id(self):
        self.assertEqual(select_table_cafedras_id(120), [0])

    def test_select_table_cafedras_titile_1(self):
        self.assertEqual(select_table_cafedras_title("kuku"), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])

    def test_select_table_cafedras_title_2(self):
        self.assertEqual(select_table_cafedras_title("dasdasdsa"), [0])

    def test_select_table_cafedras_university_1(self):
        self.assertEqual(select_table_cafedras_university("ITMO"), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])

    def test_select_table_cafedras_university_2(self):
        self.assertEqual(select_table_cafedras_university("cvcv"), [0])

    def test_select_table_cafedras_firstData_1(self):
        self.assertEqual(select_table_cafedras_firstData("2019"), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])

    def test_select_table_cafedras_firstData_2(self):
        self.assertEqual(select_table_cafedras_firstData("1514"), [0])

    def test_select_table_cafedras_secondData_1(self):
        self.assertEqual(select_table_cafedras_secondData("2021"), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])

    def test_select_table_cafedras_secondData_2(self):
        self.assertEqual(select_table_cafedras_secondData("31231"), [0])


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
    unittest.main()
