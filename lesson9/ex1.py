class product:
    def __init__(self, product_name, store_name, cost):
        self.product_name = product_name
        self.store_name = store_name
        self.cost = cost
        print("Товар: " + product_name + ". Магазин: " + store_name + ". Стоимость:", cost, "руб.") 
    
    def __add__(self, other):
        return self.cost + other.cost 
     
        
    
class storage:
    def __init__(self):
        self.products = []
       
    def product_index(self, index:int):
        if index >= 0:
            self.products[index].show()
        
    def product_for_name(self):
        pass
    
    def sort_by_name(self):
        pass
    
    def sort_by_store(self):
        pass
    
    def sort_by_cost(self):
        pass
    
    def sum_product(self):
        pass



product1 = product("Сыр", "Евроопт", 12)
product2 = product("Колбоса", "Евроопт", 9)
product3 = product("Картофель", "Корона", 1.2)
product4 = product("Томат", "Санты", 18.5)
product5 = product("Яйца", "Алми", 4)
x = product1 + product2
storage1 = storage()

print(x)