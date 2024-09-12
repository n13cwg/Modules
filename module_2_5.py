# Объявляем функцию с тремя параметрами: n (количество строк), m (количество столбцов), value (значение для заполнения)
def get_matrix(n, m, value):

    matrix = [] # Пустой список для хранения матрицы
    for i in range(n): # Проходит по каждой строке (от 0 до n - 1)
        matrix.append([]) # Пустой список для каждого элемента матрицы (строки) и добавляется в список matrix
        for j in range(m): # Проходит по каждому столбцу (от 0 до m - 1) в каждой строке
            matrix.append(value) # Заполняет список, созданный на предыдущем шаге, значением value
    return matrix # Возвращает созданный список matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)