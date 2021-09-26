from database_api import *
import unittest


class api_test(unittest.TestCase):
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

    def test_select_table_cafedras_weights(self):
        self.assertEqual(select_table_cafedras_weights(), [0, ('{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}',), ('{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}',)])

    def test_select_table_cafedras_all_rows(self):
        self.assertEqual(select_table_cafedras_all_rows(), [0, (1, 'kuku', 'ITMO', '2019', '2021', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}'), (2, 'kerker', 'SFEDU', '2015', '2013', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}')])


unittest.main()
