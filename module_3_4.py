#   Функция, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность
#   в параметр *other_words. Функция должна составить новый список same_words только из тех слов списка other_words,
#   которые содержат root_word или наоборот root_word содержит одно из этих слов.
#   После вернуть список same_words в качестве результата своей работы.
def single_root_words(root_word, *other_words):

  same_words = []
  for word in other_words: # перебирает все слова из other_words
    if root_word.lower() in word.lower() or word.lower() in root_word.lower(): # проверяет, содержит ли root_word
        # (в нижнем регистре) word (в нижнем регистре) или наоборот.
      same_words.append(word)
  return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
