def fibonacci (n):
    fib_seq=[0,1]

    if n<=0:
        return "Please enter a positive integer."
    elif n==1:
        return [0]
    elif n==2:
        return fib_seq
    
    for i in range (2,n):
        fib=fib_seq[-1]+fib_seq[-2]
        fib_seq.append(fib)
    return fib_seq

n=10
print(fibonacci(n))

