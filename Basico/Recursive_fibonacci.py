num = 10

def fast_fibonacci(n):
    if n == 0:
        return (0,1)
    else:
        a,b = fast_fibonacci(n//2)
        c = a *(b*2-a)
        d = a * a + b * b

        if (n%2) == 0: return (c,d)
        else: return (d, c+d)

print (fast_fibonacci(num))

def fibonacci(n):

    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(num)) 
    