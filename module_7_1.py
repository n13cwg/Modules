class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        if isinstance(self.name, str) and isinstance(self.weight, float) and isinstance(self.category, str):
            return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    # Метод get_products(self), считывает всю информацию из файла __file_name, закрывает его и возвращает
    # единую строку со всеми товарами из файла __file_name
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    # Метод add(self, *products), принимает неограниченное количество объектов класса Product. Добавляет в
    # файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже
    # есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
    def add(self, *products):
        current_products = self.get_products()
        for product in products:
            if product.name not in current_products:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product}\n")
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())