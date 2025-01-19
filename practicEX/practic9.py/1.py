def example(x,n):
    
    def fac(n):
        if n<1:
            return 1
        else:
            return n * fac(n-1)

    return x**n/fac(n)

print(example(4,5))