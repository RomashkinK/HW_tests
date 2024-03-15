# Задача №1 unit-tests
# Напишите тесты на любые 3 задания из 
# занятия «Коллекции данных» модуля «Основы языка программирования Python».
# Используйте своё решение домашнего задания.

from math import sqrt


def discriminant(a, b, c):
  """
  функция для нахождения дискриминанта
  """
  # Ваш алгоритм
  return b**2 - 4*a*c



def solution(a, b, c):
  """
  функция для нахождения корней уравнения
  """
  # Ваш алгоритм
  
  if discriminant(a,b,c) > 0:
    x_1 = (-b + discriminant(a,b,c) ** 0.5 )/ (2 * a)
    x_2 = (-b - discriminant(a,b,c) ** 0.5) / (2 * a)
    return (x_1, x_2)
    
  elif discriminant(a,b,c) == 0:
    x = -b / (2*a)
    return (x)
    
  else:
    return ("корней нет") 

if __name__ == '__main__':
  solution(1, 8, 15) 
  solution(1, -13, 12)
  solution(-4, 28, -49)
  solution(1, 1, 1)