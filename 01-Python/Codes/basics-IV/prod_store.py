class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):#instance method
        print(f"This {self.name} costs {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product in the store={cls.count}")
    
    @staticmethod
    def get_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted price={final_price}")
        

p1=Product("Iphone 17",83_000)
p2=Product("Iphone 16",60_000)
p3=Product("Iphone 15",52_000)
p4=Product("Iphone 14",45_000)
p1.get_info()
p2.get_info()
p3.get_info()
p4.get_info()

Product.get_count()
p1.get_discount(p1.price,7)