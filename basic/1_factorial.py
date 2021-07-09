

def factorial(n, printit=False):
    fac = 1 if (n==1 or n==0) else n * factorial(n-1, printit=printit)
    if printit:
        print (str(fac)) 
    return fac


factorial(20,True)