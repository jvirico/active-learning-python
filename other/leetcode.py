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