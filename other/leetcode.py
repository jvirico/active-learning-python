# Given a binary array, find the maximum number of consecutive 1s in this array.
def answer(list):
    max1s = 0
    count = 0
    for i in range(len(list)):
        if(list[i]==1):
            count +=1
        else:
            if count > max1s:
                max1s = count
            count = 0
    if(count>max1s): max1s = count
    return max1s

L = [1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0] # answer is 4
print(answer([1,1,0,1,1,1]))
print('next')

# Duplicate zeros
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
#Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

def duplicateZeros(arr):
    
    L = []
    length = len(arr)
    for i in arr:
        if(len(L)< length):
            if(i == 0):
                L.append(0)
                L.append(0)
            else:
                L.append(i)
        else:
            arr.clear()
            arr.extend(L)
            if(len(arr)> length):
                arr.pop()
            break

    return arr



print(duplicateZeros(list([0,0,0,0,0])))



'''
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
'''
def removeElement(nums,val):
    
    j = 0
    k = len(nums)
    for i in range(len(nums)):
        if (nums[i]!= val):
            nums[j]=nums[i]
            j+=1
        else:
            k-=1
    return k


print(removeElement([0,1,2,2,3,0,4,2],2))

def removeDuplicates(nums):
    
    j=0
    k = len(nums)
    aux = 0
    for i in range(len(nums)):
        if(i==0):
            aux = nums[i]
            j+=1
            #k-=1
        else:
            if(nums[i]==aux):
                k-=1
            else:
                nums[j]=nums[i]
                j+=1
                aux = nums[i]
    return k

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def checkIfExists(arr):
    doubles = [x*2 for x in arr]
    zeros = 0
    for i in arr:
        if i == 0: zeros+=1
        if(i in doubles and i != 0):
            return True
        elif( i in doubles and i == 0 and zeros > 1):
            return True
    return False

print(checkIfExists([-2,0,10,-19,4,6,-8]))

## Merge Sorted Array
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


def merge2(left,right):

    if len(left)==0: return right
    if len(right)==0: return left
    
    result = []
    index_left = index_right = 0
    
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge(nums1,m,nums2,n):
    nums1[m:]=nums2

    #return sorted(nums1)
    midpoint = len(nums1) // 2
    print('midpoint is %s'% midpoint)

    return merge2(nums1[:midpoint],nums1[midpoint:])




print(merge([1,2,3,0,0,0],3,[2,5,6],3))



# binary gap
def solution(N):
    bN = bin(N)[2:]

    print(bN)

    maxlen = 0
    auxlen = 0
    inBetween = False
    for i in range(len(bN)):
        if(bN[i]=='1'):
            maxlen=auxlen if auxlen>maxlen else maxlen
            auxlen = 0
        elif(bN[i]=='0'):
            auxlen+=1
        else:
            auxlen=0

    return maxlen


print(solution(100))

def solution2(A,K):

    if(len(A)==K):
        retorno = A
    else:
        B = A.copy()
        for i in range(len(A)):
            b_index = (i+K) % len(A)
            B[b_index-1] = A[i]

    return B

print(solution2([1,2,3,4],2))


def solution3(A):
    D = {}
    odd = None
    for i in range(len(A)):
        if not A[i] in D:
            L = []
            L.append(i)
            D[A[i]]=L
        else:
            D[A[i]].append(i)
        if(len(D[A[i]])%2 != 0):
            odd = i
    if(odd is not None):
        return odd
    else:
        for i in D:
            if(len(D[i])%2!=0):
                return i

A={}
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 9
A[6] = 9

print(solution3(A))

import math

def solution4(X,Y,D):
    normalized = Y-X
    jumps = normalized / D
    return math.ceil(jumps)

print(solution4(10,85,30))


def solution5(A):
    if len(A)==0:
        return 1
    else:
        L = sorted(A)
        for i in range(len(A)):
            if L[i]!= i+1:
                return i+1
        return len(A)+1

A = [2,3,1,5]
print(solution5(A))
print(solution5([]))
B=[1]
print(solution5(B))


# performance issues O(N*N)
def solution6(A):

    min = sum(list(map(abs,A)))

    for i in range(len(A)):
        if i > 0:
            left = sum(A[:i])
            right = sum(A[i:])
            dif = abs(left - right)
            if dif < min: min = dif

    return min

A = [-1000,1000]
A = [3,1,2,4,3]
print(solution6(A))

'''def solution7(A):

    all_difs = list(map(lambda x: ,A))

A = [3,1,2,4,3]
print(solution7(A))'''

'''
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
'''
def removeElement(nums,val):
    
    j = 0
    k = len(nums)
    for i in range(len(nums)):
        if (nums[i]!= val):
            nums[j]=nums[i]
            j+=1
        else:
            k-=1
    return k


print(removeElement([0,1,2,2,3,0,4,2],2))

def removeDuplicates(nums):
    
    j=0
    k = len(nums)
    aux = 0
    for i in range(len(nums)):
        if(i==0):
            aux = nums[i]
            j+=1
            #k-=1
        else:
            if(nums[i]==aux):
                k-=1
            else:
                nums[j]=nums[i]
                j+=1
                aux = nums[i]
    return k

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def checkIfExists(arr):
    doubles = [x*2 for x in arr]
    zeros = 0
    for i in arr:
        if i == 0: zeros+=1
        if(i in doubles and i != 0):
            return True
        elif( i in doubles and i == 0 and zeros > 1):
            return True
    return False

print(checkIfExists([-2,0,10,-19,4,6,-8]))



def validMountainArray(arr):
    
    pic = False
    climbed = False
    unclimbed = False
    j = arr[0]
    first = True
    for i in arr:
        
        if not first:
            # valley case
            if i==j: return False
            # climbing case (j<i) and not pic
            if (j<i and not pic): climbed = True
            # pic case
            if(not pic and i < j):
                # found pic
                pic = True
            # down hill case
            if(i<j and pic): unclimbed = True
            if(pic and i > j):
                return False
        first = False
        j = i
    return True if pic and climbed and unclimbed else False

print(validMountainArray([3,2,1]))


def replaceelements(arr):
    
    l = len(arr)
    for i in range(l):
            if(i<l-1):
                arr[i] = max(arr[i+1:])
            else:
                arr[i] = -1
    return arr


print(replaceelements([17,18,5,4,6,1]))


def replaceelements_efficient(arr):
    # minimize max function time by looping backwards and computing max of only two numbers, new and old_max
    l = len(arr)
    #new = arr.copy()
    #new[-1] = -1
    old_max = -1
    for i in reversed(range(l)):
        old_max, arr[i] = max(arr[i], old_max), old_max
    arr[l-1]=-1
    return arr

print(replaceelements_efficient([17,18,5,4,6,1]))



def moveZeros(nums):
    
    j = 0
    for i in range(len(nums)):
        num = nums[i]
        if num!=0 and i != j:
            nums[j] = num
            nums[i]=0
        if num!=0:
            j+=1
    return nums


print(moveZeros([0,1,0,3,12]))


def sortArrayByParity(nums):

    evens=0
    odds=len(nums)-1
    for i in range(len(nums)):
        if evens + odds == len(nums): break
        num = nums[i]
        if num%2 == 0:
            # even
            odds+=1 if nums[evens]%2!=0 else odds
            nums[i]=nums[evens]
            nums[evens]=num
            evens+=1
        else:
            # odd
            evens-=1 if nums[odds]%2==0 else evens
            nums[i]=nums[odds]
            nums[odds]=num
            odds-=1
    
    return nums

print(sortArrayByParity([3,1,2,4]))

def sortArrayByParity2(nums):
    left=0
    right=len(nums)-1

    while left < right:
        num=nums[left]
        if num%2==0:
            left+=1
        else:
            if nums[right]%2==0:
                nums[left]=nums[right]
                nums[right]=num
                right-=1
            else:
                right-=1
    return nums

print(sortArrayByParity2([1,3,2,4]))