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