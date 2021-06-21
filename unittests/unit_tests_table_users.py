from database_api import *
import mysql.connector
import unittest
import datetime


class api_test(unittest.TestCase):
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


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
    unittest.main()