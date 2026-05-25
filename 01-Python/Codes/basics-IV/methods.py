class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.storage=Storage
    
    def get_info(self):
        print(f"The RAM for this laptop is {self.RAM} and storage is {self.storage} {self.storage_type} ")

    
l1=Laptop("16gb","512gb")
l2=Laptop("24gb","256gb")

l1.get_info()
