def fibonacci(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
for i in range (1,101):
    print (fibonacci(i))