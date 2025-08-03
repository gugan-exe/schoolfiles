def divide(a,b):
    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))
    if b==0:
        return"Cannot divide a number by zero"
    return a/b,a,b
    

result,a,b=divide("a","b")
print(result,a,b)