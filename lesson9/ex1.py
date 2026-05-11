class product:
    def __init__(self, product_name, store_name, cost):
        self.product_name = product_name
        self.store_name = store_name
        self.cost = cost
        #print("Товар: " + product_name + ". Магазин: " + store_name + ". Стоимость:", cost, "руб.") 
    
    def __add__(self, other):
        return self.cost + other.cost 
     
    def show(self):
        print("Товар: " + self.product_name + ". Магазин: " + self.store_name + ". Стоимость:", self.cost, "руб.") 
        
    
class storage:
    def __init__(self):
        self.products = []
    
    def storage_dict(self, prod):
        self.products.append(prod)
       
    def product_index(self):
        if index >= 0:
            self.products[index].show()
        else:
            print("что то не то")
            
        
    def product_for_name(self):
        for x in self.products:
            if x.product_name == find_name:
                x.show()                     
    
    def sort_by_product_name(self):
        self.products.sort(key=lambda x: x.product_name) #ИИ
    
    def sort_by_store(self):
        self.products.sort(key=lambda x: x.store_name) 
    
    def sort_by_cost(self):
        self.products.sort(key=lambda x: x.cost)
    
    def show_all(self):
        for prod in self.products:
            prod.show()
           
index = 3
find_name = "Картофель"

storage1 = storage()

product1 = product("Сыр", "Евроопт", 12)
product2 = product("Колбоса", "Евроопт", 9)
product3 = product("Картофель", "Корона", 1.2)
product4 = product("Томат", "Санты", 18.5)
product5 = product("Яйца", "Алми", 4)

storage1.storage_dict(product1)
storage1.storage_dict(product2)
storage1.storage_dict(product3)
storage1.storage_dict(product4)
storage1.storage_dict(product5)

storage1.product_index()

print("*" * 20)

storage1.product_for_name()

print("*" * 20)
print("Сортировка по продуктам:\n ")

storage1.sort_by_product_name()
storage1.show_all()

print("*" * 20)
print("Сортировка по магазинам \n")

storage1.sort_by_store()
storage1.show_all()

print("*" * 20)
print("Сортировка по стоимости: \n")
storage1.sort_by_cost()
storage1.show_all()


x = product1 + product2


print("*" * 20)
print("Сумма стоимости товаров: ", product1 + product2)


