import math

points = [[0.0, 25.0], [12.307692307692308, 15.384615384615383], [-12.5, 25.0], [-15.333333333333332, 19.333333333333336],[10,20]]
angles = []

for index in range(len(points)):
    starting_point = points[0]
    theta = math.degrees(math.atan2((points[index][1] - starting_point[1]),(points[index][0] - starting_point[0])))
    angles.append(theta)

def swap(array,i,j):
    """
    This function will swap two variables
    """
    array[i],array[j] = array[j],array[i]



#sorting angles---------------------------------------------
temporary_number = 0
while(temporary_number < len(angles)-1):
    if(angles[temporary_number]>angles[temporary_number+1]):
        swap(angles,temporary_number,temporary_number+1)
        swap(points,temporary_number,temporary_number+1)
        temporary_number = -1 
    temporary_number+= 1


points2 =[[-15.333333333333332, 19.333333333333336], [12.307692307692308, 15.384615384615383], [10, 20], [0.0, 25.0], [-12.5, 25.0],[-15.333333333333332, 19.333333333333336]]

det = 0
for index in range(len(points2)-1):
    det += (points2[index][0]*points2[index+1][1]) - (points2[index][1]*points2[index+1][0])
    
print(det/2)




