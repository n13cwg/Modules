# file_name - название файла для записи, strings - список строк для записи
def custom_write(file_name, strings):
    strings_positions = {}
    # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings): #  с помощью enumerate, получаем индекс каждой строки i
        position = file.tell() # получаем текущую позицию курсора в файле с помощью file.tell() и сохраняем ее в
        # переменную position
        file.write(f"{string}\n") # записываем строку в файл
        strings_positions[(i, position)] = string # сохраняем в словарь strings_positions кортеж (i, position) - 
        # номер строки и позиция) как ключ, а саму строку `string` как значение.
    return strings_positions # возвращаем словарь


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)