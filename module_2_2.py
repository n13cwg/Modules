first = int(input('Первое целое число: '))
second = int(input('Второе целое число: '))
third = int(input('Третье целое число: '))

if first == second and first == third and second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
elif first == second or first == third or second == third:
    print(2)