def find_password(n): # n - число, отображаемое в первой вставке ворот
    result = "" # пустая строка для хранения пароля
    for i in range(1, 21): # перебрать все возможные пары чисел i и j от 1 до 20
        for j in range(1, 21):
            if (i + j) % n == 0 and i != n and j != n:
                result = str(i) + str(j) # сохраняет пароль
                return result
    return "Пароль не найден"