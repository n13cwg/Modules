def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [9, 3.14, 'string']
values_dict = {'a': 7, 'b': False, 'c': 'name'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Alexandra', 13]

print_params(*values_list_2, 42)