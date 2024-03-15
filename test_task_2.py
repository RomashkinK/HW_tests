import unittest
from unittest import TestCase
from task_2 import add_folder

class TestFolderCreation(TestCase):
# Проверяем результат создания папки, должен быть 201
    def test_API_positive(self):
        folder_name = 'unittest'
        ya_token = ''
        self.assertEqual(add_folder(folder_name, ya_token), 201)
# Проверяем результат повторного создания папки, должен быть 409
    def test_API_negative(self):
        folder_name = 'unittest'
        ya_token = ''
        self.assertNotEqual(add_folder(folder_name, ya_token), 409)


if __name__ == '__main__':

    unittest.main()
