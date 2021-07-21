'''
    Finding the sum of elements of an array
'''

# driver function
arr = []

def arr_sum(arr):
    result = 0.0
    for i in range(len(arr)): result += arr[i]
    return result

arr = [1,2,3,4]

print(arr_sum(arr))

'''
    Largest element in an array
'''

def the_big(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i]> max: max = arr[i]
    return max

print('Max in %s is %s'% (arr,the_big(arr)))



'''
    Array rotation d elements to the left
'''
import numpy as np

def rotate(arr,d):
    return arr[d:] + arr[:d]

print(rotate(arr,2))


'''
    Check if array is monotone increasing
    i <= j then arr[i] <= arr[j]
'''

def is_monotone_increasing(arr):

    retorno = True
    prev = arr[0]
    for i in range(len(arr)):
        if (arr[i]<prev):
            retorno = False
        prev = arr[i]

    return retorno

print('Is %s monotone increasing?: %s' % (arr,is_monotone_increasing(arr)))