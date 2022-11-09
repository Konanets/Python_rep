def menu():
    print('''1. найти min число в листе
2. удалить все одинаковые значения
3. заменить каждое 4 значение на 'X'
4. вывести елементы листа, значение которого ближе всего к середнему арифметическому всех
6. выход ''')

    number_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

    chose = input('сделайте свой выбор ')
    if chose == "1":
        print(number_list)
        print(min(number_list))
    elif chose == "2":
        print(number_list)
        print(list(set(number_list)))
    elif chose == "3":
        count = 3
        new = number_list.copy()
        while (count < len(new)):
            print(new)
            new[count] = 'X'
            count += 4
            print(number_list)
            print(new)
    elif chose == "4":
        print(number_list)
        print(sum(number_list) / len(number_list))
    elif chose == "6":
        return
    else:
        print('wrong!')
    menu()


menu()

