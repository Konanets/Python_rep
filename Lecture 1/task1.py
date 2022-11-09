import re

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'

new_st = [i for i in st if i.isdigit()]

print(*new_st, sep=',')

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34 '

new2_st = []
word = ''
for i in st:
    if i.isdigit():
        word += i
    else:
        if word != '':
            new2_st.append(word)
            word = ''

print(*new2_st, sep=', ')

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

print([word.upper() for word in greeting])

# 2) з диапозону від 0-50 записати тільки НЕ ПАРНІ ЧИСЛА при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]


numbers = [num * num for num in range(0, 50) if num % 2 != 0]

print(numbers)


# function
#
# - створити функцію яка виводить ліст

def system_out_println(ls):
    for number in ls:
        print(number, end='~')
    # print(ls)


system_out_println([1, 2, 3, 4, 5, 6, 7])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def my_max(a, b, c):
    print(max(a, b, c))

    return max(a, b, c)


my_max(5, 4, 7)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def max_and_min(*args):
    print(max(args))

    return min(args)


print(max_and_min(1, 4, 5, 2, 7, 6, 4))


# - створити функцію яка повертає найбільше число з ліста

def max_from_list(numbers):
    return max(numbers)


print(max_from_list([3, 5, 2, 67, 8, 5, 3]))


# - створити функцію яка повертає найменьше число з ліста

def min_from_list(numbers):
    return min(numbers)


print(min_from_list([12, 3, -1, 5, 5, 36, 23, 6, 236, 32]))


# - створити функцію яка приймає ліст чисел та ск`ладає значення елементів ліста та повертає його.

def sum_list(digits):
    suma = 0

    for number in digits:
        suma += number

    return suma


arr = [23523, 352, 235, 235, 233, 5]

print(sum_list(arr))


# sum([1,2,3,4,5...])

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg(digits):
    return sum(digits) / len(digits)


print(avg([1, 2, 3, 4, 5]))

#################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'


number_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(min(number_list))
number_list = list(set(number_list))
print(number_list)

count = 3
while (count < len(number_list)):
    number_list[count] = 'X'
    count += 4
print(number_list)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


def print_square(n):
    if n <= 2:
        return print('bib bop')
    print('*' * n)
    for i in range(1, n - 1):
        print('*' + ' ' * (n - 2) + '*')
    print('*' * n)


print_square(3)

# 3) вывести табличку множення за допомогою цикла while

i = 1
while i != 10:
    print('{} {} {} {} {} {} {} {} {}'.format(*[i * number for number in range(1, 10)]))
    i += 1

# 4) переробити це завдання під меню
