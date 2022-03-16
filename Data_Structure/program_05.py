#  Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity:O(n)
# Sample: [1,0,2,2,0,1,0,1,2,0,0]
# Output: [0,0,0,0,0,1,1,1,2,2,2]

array = [1,0,2,2,0,1,0,1,2,0,0]

def swap(array,i,j):
    """
    This function will swap two variables
    """
    array[i],array[j] = array[j],array[i]

def sort_array(list_of_numbers):
    '''
    This function will sort the array
    '''
    temporary_number = 0
    while(temporary_number < len(list_of_numbers)-1):
        if(list_of_numbers[temporary_number]>list_of_numbers[temporary_number+1]):
            swap(list_of_numbers,temporary_number,temporary_number+1)
            temporary_number = -1 
        temporary_number+= 1
    return list_of_numbers
print(sort_array(array))