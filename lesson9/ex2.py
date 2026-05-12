class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee < self.elephant:
            return False
        else: 
            return True
        
    
    def trumpet(self):
        if self.elephant < self.bee:
            return "wzzzzz"
        else:
            return "tu-tu-doo-doo"
    
    def eat(self, meal, value):
        self.meal = meal
        self.value = value
        
        if meal == "nectar":
            bee = self.bee + value
            elephant = self.elephant - value            
            
            if bee > 100:
                bee = 100                
                
                if elephant < 0:
                    elephant = 0
                    print(bee, elephant)
                print(bee, elephant)           
            else:
                print(bee, elephant)
                        
        elif meal == "grass":
            bee = self.bee - value
            elephant = self.elephant + value
            
            if elephant > 100:
                elephant = 100                
                
                if bee < 0:
                    bee = 0
                    print(bee, elephant)
                print(bee, elephant)            
            else:
                print(bee, elephant)
            
        else: 
            raise ValueError("Неверно введена еда")
        
        

in_date = BeeElephant(80,55)

print(in_date.fly())
print(in_date.trumpet())
in_date.eat("nectar", 19)
