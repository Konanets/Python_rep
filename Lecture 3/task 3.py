# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Reactangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return self.x + self.y


reactangle1 = Reactangle(3, 5)
reactangle2 = Reactangle(7, 8)

print(reactangle1 + reactangle2)
print(reactangle1 - reactangle2)
print(reactangle1 == reactangle2)
print(reactangle1 != reactangle2)
print(reactangle1 < reactangle2)
print(reactangle1 > reactangle2)
print(len(reactangle1))
print(len(reactangle2))


# ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.__count += 1

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, shoe size: {self.shoe_size}'


class Prince(Human):
    def __init__(self, name, age, shoe_found):
        super().__init__(name, age)
        self.shoe_found = shoe_found

    def find_cinderella(self, cinderellas: list[Cinderella, ...]):
        for cinderella in cinderellas:
            if cinderella.shoe_size == self.shoe_found:
                print(cinderella)
                break


list_of_cinderellas: list[Cinderella, ...] = [
    Cinderella('Elizabet', 23, 41),
    Cinderella('Eli', 18, 42),
    Cinderella('Beta', 19, 43),
    Cinderella('Marg', 25, 44),
    Cinderella('Eva', 46, 45),
]

prince = Prince('Viliam', 25, 43)

prince.find_cinderella(list_of_cinderellas)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    __printable_list = []

    @staticmethod
    def add(other):
        if isinstance(other, Magazine):
            Main.__printable_list.append(other)
        elif isinstance(other, Book):
            Main.__printable_list.append(other)

    @staticmethod
    def show_all_magazines():
        for item in Main.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @staticmethod
    def show_all_books():
        for item in Main.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('New York Time'))
Main.add(Magazine('Pravda Ua'))
Main.add(Magazine('Polonia'))
Main.add(Magazine('France 24'))

Main.add(Book('Discipline is freedom'))
Main.add(Book('war and peace'))
Main.add(Book('New World Order'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
