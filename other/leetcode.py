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

