# data - любой тип данных (список, кортеж, словарь, строка, число, множество)
def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)

    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, str):
                total_sum += len(key)  # Суммируем длину строковых ключей
            total_sum += calculate_structure_sum(value)

    elif isinstance(data, str):
        total_sum += len(data)  # Суммируем длину строк

    elif isinstance(data, (int, float)):
        total_sum += data  # Суммируем числа

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)