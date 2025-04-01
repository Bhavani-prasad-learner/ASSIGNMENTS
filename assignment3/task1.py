#Task 1: Calculate Factorial Using a Function
num=int(input("enter a number : "))
def factorial(num):
    if(num<=1):
        return 1
    else:
        return num*factorial(num-1)
print("factorial of ",num,"is :",factorial(num))
    