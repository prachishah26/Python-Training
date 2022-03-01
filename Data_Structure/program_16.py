# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8

array = [1, 5, 1, 10, 50]
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

required_num = sort_array(array)[-1]
print(required_num)