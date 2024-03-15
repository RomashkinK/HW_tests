import unittest
from task_1_1 import solution
from task_1_2 import vote
from task_1_3 import get_name, get_directory, add

def test_task_1_1(a, b, c, expected):
    result = solution(a, b, c)
    try:
        assert result == expected
        print(f'Test for {a}, {b}, {c} passed with result {result}')
    except AssertionError:
        print(f'Test for {a}, {b}, {c} failed. Correct result {result}')


def test_task_1_2(votes, expected):
    result = vote(votes)
    try:
        assert result == expected
        print(f'Test for {votes} passed with result {result}')
    except AssertionError:
        print(f'Test for {votes} failed. Correct result {result}')


def test_task_1_3_get_name(doc_number, expected):
    result = get_name(doc_number)
    try:
        assert result == expected
        print(f'Test for {doc_number} passed with result {result}')
    except AssertionError:
        print(f'Test for {doc_number} failed. Correct result {result}')


def test_task_1_3_get_directory(doc_number, expected):
    result = get_directory(doc_number)
    try:
        assert result == expected
        print(f'Test for {doc_number} passed with result {result}')
    except AssertionError:
        print(f'Test for {doc_number} failed. Correct result {result}')




if __name__ == "__main__":

    test_task_1_1(1, -13, 12, (12.5, 1.0))
    test_task_1_1(-4, 28, -49, 3.5)
    test_task_1_1(1, 1, 1, "корней нет")


    test_task_1_2([1, 1, 1, 2, 3], 1)
    test_task_1_2([1, 2, 3, 2, 2], 2)
    test_task_1_2([1, 4, 1, 4, 4], 1)


    test_task_1_3_get_name("10006", "Аристарх Павлов")
    test_task_1_3_get_name("11-2", "Иванов Иван")

    test_task_1_3_get_directory("10006", "2")
    test_task_1_3_get_directory("11-2", "3")






