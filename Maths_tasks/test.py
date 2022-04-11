
import numpy as np
import math
import time
np.seterr(divide='ignore', invalid='ignore')

def intersecting(p1,q1,p2,q2):
    """
    This function will give the intersecting points between two line segments.
    """
    intersecting_points = []
    p1 = np.array(p1)
    q1 = np.array(q1)
    p2 = np.array(p2)
    q2 = np.array(q2)
   
    r = q1 - p1  #distance of two points on line-1 segments.
    s = q2 - p2    ##distance of two points on line-2 segments.
    try:
        t = np.cross((p2 - p1),s)/np.cross(r,s)
        u = np.cross((p1-p2),r)/np.cross(s,r)

        t0 = np.dot((p2-p1),r)/np.dot(r,r)
        t1 = np.dot((p2 + s - p1),r)/np.dot(r,r)
    
    except Exception as e:
            pass
    else:
        if np.cross(r,s) != 0 and t >= 0 and t <= 1 and u >= 0 and u <= 1:
            # print("Line segments are intersecting at points: ",p1 + t*r)
            point = p1 + t*r
            if point not in intersecting_points:
                intersecting_points.append(point)

        if np.cross(r,s) == 0 and np.cross((p2-p1),r) == 0 :
            if (t0<=1 and t0 >=0) or (t1<=1 and t1 >=0) :
                # print("Lines are colinear and overlapping")
                # print(q2,q1)
                if ((p2[0]>=p1[0] and p2[0] <= q1[0]) or (p2[0]<=p1[0] and p2[0] >= q1[0])) and ((p2[1]>=p1[1] and p2[1] <= q1[1]) or (p2[1]<=p1[1] and p2[1] >= q1[1])):
                    print("Overlapping point : ",p2)
                    if p2 not in intersecting_points:
                        intersecting_points.append(p2)

                if ((q2[0]>=p1[0] and q2[0] <= q1[0]) or (q2[0]<=p1[0] and q2[0] >= q1[0])) and ((q2[1]>=p1[1] and q2[1] <= q1[1]) or (q2[1]<=p1[1] and q2[1] >= q1[1])):
                    # print("Overlapping point : ",q2)
                    if q2 not in intersecting_points:
                        intersecting_points.append(q2)

                if ((q1[0]>=p2[0] and q1[0] <= q2[0]) or (q1[0]<=p2[0] and q1[0] >= q2[0])) and ((q1[1]>=p2[1] and q1[1] <= q2[1]) or (q1[1]<=p2[1] and q1[1] >= q2[1])):
                    # print("Overlapping point : ",q1)
                    if q1 not in intersecting_points:
                        intersecting_points.append(q1)

                if ((p1[0]>=p2[0] and p1[0] <= q2[0]) or (p1[0]<=p2[0] and p1[0] >= q2[0])) and ((p1[1]>=p2[1] and p1[1] <= q2[1]) or (p1[1]<=p2[1] and p1[1] >= q2[1])):
                    # print("Overlapping point : ",p1)
                    if p1 not in intersecting_points:
                        intersecting_points.append(p1)
    return intersecting_points
   
def intersecting_points_polygon(polygon1, polygon2):
    """
    This function will give intersecting points of two polygon.
    """

    length1 = len(polygon1)-1
    length2 = len(polygon2)-1
    line= []
    intersecting_points = []

    for i in range(len(polygon1)):
        for j in range(len(polygon2)):
            if i < length1 and j < length2 :
                # print(polygon1[i],polygon1[i+1],polygon2[j],polygon2[j+1])
                line.append(polygon1[i])
                line.append(polygon1[i+1])
                line.append(polygon2[j])
                line.append(polygon2[j+1])
                
                
                p1 = np.array(line[0])
                q1 = np.array(line[1])
                
                p2 = np.array(line[2])
                q2 = np.array(line[3])
                
                # print(p1,q1,p2,q2)
                r = q1 - p1
                s = q2 - p2
                try:
                    t = np.cross((p2 - p1),s)/np.cross(r,s)
                    u = np.cross((p1-p2),r)/np.cross(s,r)

                    t0 = np.dot((p2-p1),r)/np.dot(r,r)
                    t1 = np.dot((p2 + s - p1),r)/np.dot(r,r)
                
                except ZeroDivisionError as e:
                        pass
                else:
                    if np.cross(r,s) != 0 and t >= 0 and t <= 1 and u >= 0 and u <= 1:
                        # print("Line segments are intersecting at points: ",p1 + t*r)
                        point = p1 + t*r
                        if list(point) not in intersecting_points:
                            intersecting_points.append(list(point))

                    #for colinear points
                    if np.cross(r,s) == 0 and np.cross((p2-p1),r) == 0 :
                        if (t0<=1 and t0 >=0) or (t1<=1 and t1 >=0) :
                            # print("Lines are colinear and overlapping")
                            # print(q2,q1)
                            if ((p2[0]>=p1[0] and p2[0] <= q1[0]) or (p2[0]<=p1[0] and p2[0] >= q1[0])) and ((p2[1]>=p1[1] and p2[1] <= q1[1]) or (p2[1]<=p1[1] and p2[1] >= q1[1])):
                                # print("Overlapping point : ",p2)
                                if list(p2) not in intersecting_points:
                                    intersecting_points.append(list(p2))

                            if ((q2[0]>=p1[0] and q2[0] <= q1[0]) or (q2[0]<=p1[0] and q2[0] >= q1[0])) and ((q2[1]>=p1[1] and q2[1] <= q1[1]) or (q2[1]<=p1[1] and q2[1] >= q1[1])):
                                # print("Overlapping point : ",q2)
                                if list(q2) not in intersecting_points:
                                    intersecting_points.append(list(q2))

                            if ((q1[0]>=p2[0] and q1[0] <= q2[0]) or (q1[0]<=p2[0] and q1[0] >= q2[0])) and ((q1[1]>=p2[1] and q1[1] <= q2[1]) or (q1[1]<=p2[1] and q1[1] >= q2[1])):
                                # print("Overlapping point : ",q1)
                                if list(q1) not in intersecting_points:
                                    intersecting_points.append(list(q1))

                            if ((p1[0]>=p2[0] and p1[0] <= q2[0]) or (p1[0]<=p2[0] and p1[0] >= q2[0])) and ((p1[1]>=p2[1] and p1[1] <= q2[1]) or (p1[1]<=p2[1] and p1[1] >= q2[1])):
                                # print("Overlapping point : ",p1)
                                if list(p1) not in intersecting_points:
                                    intersecting_points.append(list(p1))
                        
                
            line.clear()
    return intersecting_points

def swap(array,i,j):
    """
    This function will swap two variables
    """
    array[i],array[j] = array[j],array[i]

def finding_angles(intersecting_points):
    """
    This function will find the angles of all the coordinates with respect to one point. 
    """
    angles = []
    for index in range(len(intersecting_points)):
        starting_point = intersecting_points[0]
        theta = math.degrees(math.atan2((intersecting_points[index][1] - starting_point[1]),(intersecting_points[index][0] - starting_point[0])))
        angles.append(theta)
    return angles

def find_area(points_of_polygon):
    """
    This function will find the area of polygon
    """
    determinant = 0
    for index in range(len(points_of_polygon)-1):
        determinant += (points_of_polygon[index][0]*points_of_polygon[index+1][1]) - (points_of_polygon[index][1]*points_of_polygon[index+1][0])
    area = 0.5 * determinant
    return area

polygon1 = [[-10, 30], [10, 20], [15, 10], [-20, 10],[-10, 30]]
polygon2 = [[-20, 25], [15, 25], [15, 15], [-20, 20],[-20, 25]]

# polygon1 = [[-10,30],[-5,35],[10,20],[15, 10],[-20,10],[-20,20],[-10,30]]
# polygon2 = [[-25,25],[-20,30],[-5,35],[15,25],[15,20],[-30,20],[-25,25]]

# polygon1 = [[-10,30],[10,20],[15,10],[-20,10],[-10,30]]
# polygon2 = [[20,25],[15,25],[15,15],[20,20],[20,25]]

intersecting_points = intersecting_points_polygon(polygon1, polygon2)

# polygon1 = [[-10,30],[-5,35],[10,20],[15, 10],[-20,10],[-20,20],[-10,30]]
# polygon2 = [[-25,25],[-20,30],[-5,35],[15,25],[15,20],[-30,20]]

polygon2 = [[-10, 30], [10, 20], [15, 10], [-20, 10]]
polygon1 = [[-20, 25], [15, 25], [15, 15], [-20, 20],[-20,25]]

# polygon1 = [[-10,30],[10,20],[15,10],[-20,10],[-10,30]]
# polygon2 = [[20,25],[15,25],[15,15],[20,20]]

my_list = []
count1 = 0 
count2 = 0

for i in range(len(polygon2)):
    point_x1 = np.array(polygon2[i])
    point_x2 = np.array([1000000,polygon2[i][1]])

    point_y1 = np.array(polygon2[i])
    point_y2 = np.array([-1000000,polygon2[i][1]])

    for j in range(len(polygon1)-1):

        if intersecting(polygon1[j],polygon1[j+1],point_x1,point_x2)  :
            count1 += 1
            # my_list.append(point_x1)
        if intersecting(polygon1[j],polygon1[j+1],point_y1,point_y2)  :
            count2 += 1
        if count1 and count2:
            if point_x1 not in my_list:
                my_list.append(point_x1)
    count1 = 0
    count2 = 0

for i in range(len(my_list)):
    intersecting_points.append(my_list[i])

#sorting angles---------------------------------------------

angles = finding_angles(intersecting_points)
temporary_number = 0
starting_time = time.time()
print("--",angles)
while(temporary_number < len(angles)-1):
    if(angles[temporary_number]>angles[temporary_number+1]):
        swap(angles,temporary_number,temporary_number+1)
        swap(intersecting_points,temporary_number,temporary_number+1)
        temporary_number = -1 
    temporary_number+= 1
print(time.time() - starting_time)


#finding area of overlapping polygon------------------------

intersecting_points.append(intersecting_points[0])
if len(intersecting_points) == 0:
    print("No overlapping")
else:
    print(find_area(intersecting_points))


