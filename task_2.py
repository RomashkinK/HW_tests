# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. 
# Написать тесты, проверяющий создание папки на Диске.  
# Используя библиотеку requests напишите unit-test 
# на верный ответ и возможные отрицательные тесты на ответы с ошибкой

# Пример положительных тестов:
# * Код ответа соответствует 200.
# * Результат создания папки - папка появилась в списке файлов.

import requests

def add_folder(folder_name, ya_token):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'{folder_name}',
                  'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        print(response.status_code)
        return response.status_code




if __name__ == '__main__':

    folder_name = 'unit'
    ya_token = ''
    add_folder(folder_name, ya_token)