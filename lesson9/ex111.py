class Tovar:
    def __init__(self, name, shop, price):
        self.name = name
        self.shop = shop
        self.price = price

    def show(self):
        print("Товар:", self.name, "| Магазин:", self.shop, "| Цена:", self.price)

    def __add__(self, other):
        return self.price + other.price


class Sklad:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find_by_index(self, index):
        if index < len(self.products):
            self.products[index].show()
        else:
            print("Нет такого индекса")

    def find_by_name(self, name):
        for product in self.products:
            if product.name == name:
                product.show()
                return
        print("Товар не найден")

    def sort_by_name(self):
        self.products.sort(key=lambda x: x.name)

    def sort_by_shop(self):
        self.products.sort(key=lambda x: x.shop)

    def sort_by_price(self):
        self.products.sort(key=lambda x: x.price)

    def show_all(self):
        for product in self.products:
            product.show()
    
    

sklad = Sklad()

t1 = Tovar("Хлеб", "Евроопт", 45)
t2 = Tovar("Молоко", "Санта", 80)
t3 = Tovar("Сыр", "Корона", 150)

sklad.add(t1)
sklad.add(t2)
sklad.add(t3)

sklad.show_all()

print()
sklad.find_by_index(1)

print()
sklad.find_by_name("Сыр")

print()
sklad.sort_by_price()
sklad.show_all()

print()
print("Сумма:", t1 + t2)
