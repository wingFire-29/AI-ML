try:#trying if anything in this throws error
    x=int(input("enter x:"))
    ans=10/x
except ZeroDivisionError:#excecption error
    print(f"Divide by 0 is not allowed")    
except ValueError:
    print(f"Invalid input")
else:#execute this if no error
    print(f"ans={ans}")

finally:
    print("End of program")    