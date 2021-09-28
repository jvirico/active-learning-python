# simple recursion produces O(n) space and O(n) temporal cost
def sum(n):
    if(n == 0):
        return 0
    else:
        return n + sum(n-1)

print(sum(10))


# O(1) space O(n) temporal.
def pairSum(a,b):
    return a+b

def pairSumSequence(n):
    sum = 0
    for i in range(0,n):
        sum += pairSum(n, n+1)
    return sum

print(pairSumSequence(10))

# runtime? is O(N)
def foo(list):
    sum = 0
    product = 1
    n = len(list)
    for i in range(0,n):
        sum += list[i]
    for i in range(0,n):
        product *= list[i]
    print('sum = %s, prod = %s'% (sum,product))

foo([1,2,4,1,10])

