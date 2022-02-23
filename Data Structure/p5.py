#  Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity:O(n)
# Sample: [1,0,2,2,0,1,0,1,2,0,0]
# Output: [0,0,0,0,0,1,1,1,2,2,2]

array = [1,0,2,2,0,1,0,1,2,0,0]

def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sort_array(arr1):
    temp = 0
    while(temp < len(arr1)-1):
        if(arr1[temp]>arr1[temp+1]):
            swap(arr1,temp,temp+1)
            temp = -1 
        temp+= 1
    return arr1
print(sort_array(array))