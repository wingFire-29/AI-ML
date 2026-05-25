class Laptop:
    storage_type='ssd'

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod        #this is a decorator used for class methods
    def get_storage(cls):
        print(f"storage type={cls.storage_type}")

    def get_info(self): #instance method
        print(f"The RAM of this laptop is {self.RAM} and the storage is {self.storage} {self.storage_type}")    

    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted price={final_price}")

l1=Laptop("16gb","512gb")        
l1.calc_discount(40_000,10)