import unittest
from unittest import TestCase
from task_1_1 import solution
from task_1_2 import vote
from task_1_3 import get_name, get_directory



class TestMain(TestCase):
    def test_vote(self):
        self.assertEqual(vote([1, 1, 1, 2, 3]), 1)

    def test_solution(self):
        self.assertEqual(solution(1, -13, 12), (12.0, 1.0))

    def test_get_name(self):
        self.assertEqual(get_name('10006'), 'Аристарх Павлов')

    def test_get_name1(self):
        self.assertEqual(get_name('11-2'), 'Иванов Иван')

    def test_get_directory(self):
        self.assertEqual(get_directory('10006'), '2')

    def test_get_directory1(self):
        self.assertEqual(get_directory('11-2'), '3')



if __name__ == '__main__':

    unittest.main()


