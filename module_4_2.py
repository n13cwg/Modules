def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# Вызов inner_function вне test_function выдаст ошибку NameError: name 'inner_function' is not defined

test_function() # Вызов test_function, который вызовет inner_function
