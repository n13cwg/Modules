my_dict = {'Scott': 1, 'Alexandra': 2, 'Ryan': 3}
print(my_dict)

print(my_dict['Scott'])
print(my_dict.get('Max'))

my_dict.update({'Jeff': 4,
                'Maverick': 5})
print(my_dict)

a = my_dict.pop('Jeff')
print(a)
print(my_dict)

my_set = {1, 2, 3, 3, 2, 1, 'Scott', 'Scott', (4, 'Ya'), True}
print(my_set)

my_set.update([7, 'Anubis'])
print(my_set)

my_set.remove(2)
print(my_set)