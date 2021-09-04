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


'''
    Max consecutive ones
        Input: nums = [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

def findMaxConsecutiveOnes(nums):
    # nums is a list List[int]
    max = 0
    count = 0

    for i in range(nums):
        if i == 1:
            count+=1
        else:
            max = count if count>max else max
            count = 0
    max = count if count>max else max


'''
    Find numbers with even number of digits
'''
def findNumbers(nums):
    count = 0

    for i in nums:
        ln = len(str(i))
        if(ln%2)==0:
            count+=1

    return count

print(findNumbers([555,901,482,1771]))