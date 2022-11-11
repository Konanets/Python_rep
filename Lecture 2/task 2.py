from typing import Callable


# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append('{}) {}'.format(len(todo_list) + 1, todo))
#
#     def get_all():
#         nonlocal todo_list
#         return todo_list
#
#     return get_all, add_todo
#
#
# get_todo, add_todo = notebook()
# add_todo('Do homework')
# add_todo('learn something new')
# add_todo('go to work')
#
# print(*get_todo(), sep='\n')


# 2) протипізувати перше завдання

def notebook() -> tuple[
    Callable[[], list[str]],
    Callable[[str], None]
]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append('{}) {}'.format(len(todo_list) + 1, todo))

    def get_all() -> list[str, ...]:
        nonlocal todo_list
        return todo_list

    return get_all, add_todo


get_todo, add_todo = notebook()
add_todo('Do homework')
add_todo('learn something new')
add_todo('go to work')
print(*get_todo(), sep='\n')


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_from(string: str) -> str:
    split_str = list(string)
    length = len(split_str) - 1
    return ' + '.join([x + '0' * (length - i) for i, x in enumerate(split_str) if (x != '0')])


print(expanded_from('12'))
print(expanded_from('42'))
print(expanded_from('70304'))


def decor(func):
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        print('count: {}'.format(counter))
        func()
        print('-' * 15)

    return increment


@decor
def happy_func1():
    print('I`m happy func 1')


@decor
def happy_func2():
    print('I`m happy func 2')


happy_func1()
happy_func1()
happy_func1()

happy_func2()
happy_func2()
