class WordsFinder:
    # Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в
    # атрибут file_names в виде списка или кортежа.
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = line.strip(',', '.', '=', '!', '?', ';', ':', ' - ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его
    # слов.

    # метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
    # позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    # метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова
    # word в списке слов этого файла.
    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего