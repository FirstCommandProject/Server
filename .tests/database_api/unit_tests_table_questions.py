from database_api import *
import unittest


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

    def test_select_table_questions_all_rows(self):
        self.assertEqual(select_table_questions_all_rows(), [0, (1, 'Вы любите космические исследования?', '["math", "astronomy", "programming"]', '{"math": 1.5, "anatomy": 0.4, "biology": 0.4, "economy": 0.9, "business": 1, "astronomy": 1.3, "chemistry": 0.6, "geography": 1.2, "psyhology": 0.8, "engineering": 1.4, "informatics": 1.6, "linguistics": 0.6, "programming": 1.2, "political science": 0.3, "religious studies": 0.2}'), (2, 'Вам нравятся гуманитарные предметы?', '["psyhology", "linguistics", "biology", "anatomy", "religious studies", "political science", "chemistry", "business"]', '{"math": 0.5, "anatomy": 1.5, "biology": 1.5, "economy": 0.5, "business": 0.5, "astronomy": 0.5, "chemistry": 1.5, "geography": 1.5, "psyhology": 1.5, "engineering": 0.5, "informatics": 0.5, "linguistics": 1.5, "programming": 0.5, "political science": 1.5, "religious studies": 1.5}'), (3, 'Вам нравится теоретическая информатика?', '["math", "informatics", "programming", "engineering"]', '{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 0.5, "business": 1.1, "astronomy": 1.2, "chemistry": 0.5, "geography": 0.5, "psyhology": 0.7, "engineering": 1.25, "informatics": 1.6, "linguistics": 0.5, "programming": 1.4, "political science": 0.5, "religious studies": 0.5}'), (4, 'Вам нравится экономика?', '["math", "economy", "linguistics", "geography"]', '{"math": 1.4, "anatomy": 0.5, "biology": 0.5, "economy": 1.7, "business": 1.2, "astronomy": 1.2, "chemistry": 0.5, "geography": 1.2, "psyhology": 0.6, "engineering": 0.5, "informatics": 1.3, "linguistics": 0.6, "programming": 1.3, "political science": 1.5, "religious studies": 0.5}')])


unittest.main()
