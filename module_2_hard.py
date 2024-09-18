def generate_password(n):
    result = "" # Для хранения пароля
    for i in range(1, n): # Цикл перебирает числа от 1 до n-1
        for j in range(i+1, n+1): # Цикл перебирает числа от i+1 до n
            if (i + j) == n: # Проверка, кратно ли n сумме i и j
                result += str(i) + str(j) # Добавление пары чисел в строку result
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Неверный ввод числа. Число должно быть от 3 до 20.")
