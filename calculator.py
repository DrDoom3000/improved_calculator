# my_first_calculator.py by AceLewis
# Removed sub-optimal code
print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide any positive number') #Can now use any positive number
val1=input("Please enter a number:")
op=input("Please enter the operator:")
val2=input("Please enter the second number:")
int1=float(val1)    #Can use float variables
int2=float(val2)    #This one too
result=0

def calculate(int1, op, int2, result):  #Function to calculate the result
    if op =="+":
        result=int1+int2
        print(result)
    elif op =="-":
        result=int1-int2
        print(result)
    elif op =="*":
        result=int1*int2
        print(result)
    elif op =="/":
        result=int1/int2
        print(result)

calculate(int1, op, int2, result)
