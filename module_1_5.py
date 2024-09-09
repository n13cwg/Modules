immutable_var = (1, 2, 'immutable_var', [3, 4], True)
print(immutable_var)

# Кортеж это неизменяемый объект, но если он содержит изменяемые объекты, то их можно изменить. Из всех элементов можно
# изменить только список [3, 4].
immutable_var[3][1] = 7
print(immutable_var)

mutable_list = [5, 6, 'mutable_list', False]
print(mutable_list)

mutable_list.append(13)
print(mutable_list)

mutable_list[1] = 'шесть'
print(mutable_list)

mutable_list.pop(0)
print(mutable_list)