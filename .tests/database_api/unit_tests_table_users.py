from database_api import *
import unittest


class api_test(unittest.TestCase):
    def test_select_table_users_login_1(self):
        self.assertEqual(select_table_users_login("zerg12345"), [0, ('zerg12345', 'GAAGA', 'DURANT', 'ASTRONAUT', 'CAREER', 'OXFORD')])

    def test_select_table_users_login_2(self):
        self.assertEqual(select_table_users_login("DIMA123456789"), [0])

    def test_select_table_users_password_1(self):
        self.assertEqual(select_table_users_password("GG"), [0, ('kukuha', 'GG', 'Sasha', 'Kostylev', 'Valerevich', 'ITMO')])

    def test_select_table_users_password_2(self):
        self.assertEqual(select_table_users_password("PYTRPYRTY"), [0])

    def test_select_table_users_name_1(self):
        self.assertEqual(select_table_users_name("Dima"), [0])

    def test_select_table_users_name_2(self):
        self.assertEqual(select_table_users_name("KOLYA"), [0])

    def test_select_table_users_surname_1(self):
        self.assertEqual(select_table_users_surname("SVECHNIKAR"), [0])

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

    def test_upsert_table_users_login(self):
        self.assertEqual(upsert_table_users_login("kozklik", "dimasss"), [0])

    def test_upsert_table_users_password(self):
        self.assertEqual(upsert_table_users_password("zerg12345", "GAAGA"), [0])

    def test_upsert_table_users_name(self):
        self.assertEqual(upsert_table_users_name("zerg12345", "DURANT"), [0])

    def test_upsert_table_users_surname(self):
        self.assertEqual(upsert_table_users_surname("zerg12345", "ASTRONAUT"), [0])

    def test_upsert_table_users_patronymic(self):
        self.assertEqual(upsert_table_users_patronymic("zerg12345", "CAREER"), [0])

    def test_upsert_table_users_university(self):
        self.assertEqual(upsert_table_users_university("zerg12345", "OXFORD"), [0])

    def test_select_table_users_all_rows(self):
        self.assertEqual(select_table_users_all_rows(), [0, ('zerg12345', 'GAAGA', 'DURANT', 'ASTRONAUT', 'CAREER', 'OXFORD'), ('kukuha', 'GG', 'Sasha', 'Kostylev', 'Valerevich', 'ITMO'), ('kozlikk', 'kozelok', 'KOK', 'KOKER', 'iron', 'KUBGAU')])


unittest.main()
