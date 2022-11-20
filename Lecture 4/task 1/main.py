# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменомо gmail.com (Хеш то що з ліва записувати не потрібно)

try:
    with open('emails.txt') as file, open('gmails.txt', mode='w') as new_file:
        for item in file:
            email = item.split()[1]
            if email.endswith('gmail.com'):
                new_file.write(f'{email}\n')
except Exception as err:
    print(err)
