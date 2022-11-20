import json


# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

class NoteBook:
    def __init__(self):
        self.__file_path = 'notes.json'
        self.__notes = []

        try:
            with open(self.__file_path) as file:
                self.__notes = json.load(file)
        except Exception as err:
            print(err)

    def show_all(self):
        for note in self.__notes:
            print(f'{note["name"]} - {note["price"]}')

    def add(self):
        try:
            with open(self.__file_path, mode='w') as file:
                name = input('input name: ')
                price = ''
                while not price.isdigit():
                    price = input('input price: ')

                note_id = self.__notes[-1]['id'] + 1 if self.__notes else 1
                self.__notes.append({'id': note_id, 'price': int(price), 'name': name})
                json.dump(self.__notes, file)
        except Exception as err:
            print(err)

    def most_expensive(self):
        if not self.__notes:
            return
        print(max(self.__notes, key=lambda note: note['price']))

    def delete_by_id(self):

        id_for_delete = ''
        while not id_for_delete.isdigit():
            id_for_delete = input('input id for deleting: ')

        for index, note in enumerate(self.__notes):
            if note['id'] == int(id_for_delete):
                try:
                    with open(self.__file_path, mode='w') as file:
                        self.__notes.pop(index)
                        json.dump(self.__notes, file)
                except Exception as err:
                    print(err)
                break
        else:
            print('id не знайдено')

    def search(self):
        input_for_search = input('input what you search: ')
        search_list = []
        if input_for_search.isdigit():
            for note in self.__notes:
                if int(input_for_search) in (note['id'], note['price']):
                    search_list.append(note)
        else:
            for note in self.__notes:
                if input_for_search == note['name']:
                    print('tak')
                    search_list.append(note)
        if search_list:
            print(*search_list, sep='\n')
        else:
            print('Нічого не знайдено :( ')
    def menu(self):

        print("""
  1) вивід всіх покупок
  2) додати нову покупку
  3) шукати по будь якому полю
  4) показати найдорожчу покупку
  5) видалити покупку по id
  6) вихід""")

        choice = input('choose action: ')

        match choice:
            case '1':
                self.show_all()
            case '2':
                self.add()
            case '3':
                self.search()
            case '4':
                self.most_expensive()
            case '5':
                self.delete_by_id()
            case '6':
                return

        self.menu()


note_book = NoteBook()

note_book.menu()
