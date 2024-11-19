from pprint import pprint
class Product:
    def __init__(self, name, weigth, category):
        self.name=name
        self.weigth=weigth
        self.category=category
    def __str__(self):
        return (f'{self.name}, {self.weigth}, {self.category}')
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self, words):
        file = open(self.__file_name)
        pprint (file.read())
         # = open_file_name.read('self.__file_name')
        file.close()
        # return words

    def add(self, *products):
        file = open(self.__file_name)
        words = pprint (file.read())
        for i in products:
            if i in words:
                print(f'Продукт {Product.name} уже есть в магазине' )
# my_product = Product('Гречка','800 грамм','Крупа')
# print(my_product.__str__())
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())