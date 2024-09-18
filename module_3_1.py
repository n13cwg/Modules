calls = 0 # Глобальная переменная для подсчета вызовов

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция для обработки строки
def string_info(string):
    count_calls() # Увеличиваем счетчик вызовов
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return length, upper_string, lower_string

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls() # Увеличиваем счетчик вызовов
    string = string.lower() # Приводим строку к нижнему регистру
    for i in list_to_search: # Проверяет, содержится ли строка в списке
        if i.lower() == string: # Приводим строку из списка к нижнему регистру
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


