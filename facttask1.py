def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact =fact* i
        print(f"The factorial of {n} is: {fact}")

n = int(input("Enter a Number:  "))
factorial(n)
        
        
    
        
