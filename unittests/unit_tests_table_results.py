from database_api import *
import unittest
import datetime


class api_test(unittest.TestCase):
    def test_select_table_results_login_1(self):
        self.assertEqual(select_table_results_login("kerer"), [0, ('kerer', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}', datetime.datetime(2015, 5, 7, 10, 5, 23))])

    def test_select_table_results_login_2(self):
        self.assertEqual(select_table_results_login("adsadas"), [0])

    def test_select_table_results_time_1(self):
        self.assertEqual(select_table_results_time(datetime.datetime(2015, 5, 7, 10, 5, 23)), [0, ('kerer', '{"math": 1.9, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 0.2, "astronomy": 1.5, "chemistry": 0.8, "geography": 0.5, "psyhology": 0.5, "engineering": 1.8, "informatics": 1.5, "linguistics": 0.5, "programming": 1.5, "political science": 0.5, "religious studies": 0.5}', datetime.datetime(2015, 5, 7, 10, 5, 23))])

    def test_select_table_results_time_2(self):
        self.assertEqual(select_table_results_time("2015"), 1525)

    def test_insert_table_results_1(self):
        self.assertEqual(insert_table_results("zadorin", '{"math": 1.4, "culture": 2.2, "astronomy": 0.3}', "2013-05-15 11:22:23"), [0])

    def test_insert_table_results_2(self):
        self.assertEqual(insert_table_results("asdasd", {"sir": 1.2, "heh": 0.5}, "2011-05-15 11:25:24"), 1064)


unittest.main()
