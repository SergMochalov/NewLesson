
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def  __str__ (self):
           return (f"Название: {self.name}, вес: {self.weight}, категория: {self.category}.")

class Shop():
    def __init__(self, filename: str = 'products.txt'):
        self. __file_name = filename


    def get_products(self):
        file = open(self.__file_name,)
        res = file.read()
        file.close()
        return "".join(res)

    def add(self, *products: Product):
        my_products = self.get_products()
        file = open(self.__file_name, "a")
        for product in products:
            if str(product) in my_products:
                product.weight += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product.weight}.')

            else:
                file.write(f"{product}\n")
        file.close()







s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())

