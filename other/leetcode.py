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