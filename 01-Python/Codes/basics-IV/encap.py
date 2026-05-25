'''
Here i will write code related to three type of data hiding
public=var
protected=_var,this is accessible sirf naam ke protected hota h but ese bnaya variable to python m manlete h ke use ni krna bahr
private=__var,yh bhi utna private nhi h kr skte access bahr but ek bar m ni getter setters ka use krke
'''
class bankAccount:
    def __init__(self,name,balance,pin):
        self.name=name #public
        self._balance=balance #protected
        self.__pin=pin #private

    def get_pin(self): #getter
        return self.__pin
    def set_balance(self,newBalance):# setter function
        self._balance=newBalance

acc1=bankAccount("Parag","10 Million dollars",1234)
print(f"{acc1.name} has {acc1._balance} in his bank")# protected but still accessible
print(f"The pin is {acc1.get_pin()}")# way to access the private method
acc1.set_balance(2_00_000)
print(f"{acc1.name} has {acc1._balance} in his bank")# protected but still accessible
print(f"The pin is {acc1._bankAccount__pin}")#another way to access