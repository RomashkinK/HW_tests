documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    # your code
    for position in documents:
        if doc_number in position["number"]:
            return position["name"]
    return "Документ не найден"

def get_directory(doc_number):
    # your code
    for key in directories.keys():
        number_list = directories[key]
        if doc_number in number_list:
            return key
    return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
    # your code
    key = str(shelf_number)
    directories[key].append(number)
    documents.append({"type": document_type, "number": number, "name": name})




if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))