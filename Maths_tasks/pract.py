
INT_MAX = 10000
def orientation(p,q,other_point):
    orientation_value = ((q[1]-p[1])*(other_point[0]- q[0]))- ((q[0]-p[0])*(other_point[1]-q[1]))
    # print(orientation_value)
    if orientation_value > 0:
        return 1   #positive side
    elif orientation_value < 0:
        return -1  #negative side
    else:
        return 0

# for colinear points------------------------------------
def PointsOnLineSegment(p, other_point, q):
	if ( (q[0] <= max(p[0], other_point[0])) and (q[0] >= min(p[0], other_point[0])) and
		(q[1] <= max(p[1], other_point[1])) and (q[1] >= min(p[1], other_point[1]))):
		return 1
	return 0

# Checking whether line segments intersecting or not
def Intersect(p1,q1,p2,q2):
    a = orientation(p1,q1,p2)
    b = orientation(p1,q1,q2)
    c = orientation(p2,q2,p1)
    d = orientation(p2,q2,q1)

    if a == 0 and PointsOnLineSegment(p1,p2,q1) == 1:
        return "Intersecting"
    if b == 0 and PointsOnLineSegment(p1,q2,q1) == 1:
        return "Intersecting"
    if c == 0 and PointsOnLineSegment(p1,p1,q2) == 1:
        return "Intersecting"
    if c == 0 and PointsOnLineSegment(p2,q2,q1) == 1:
        return "Intersecting"
    if a != b and c != d:
        return "Intersecting"
    
    return "Not Intersecting"

# starting_point1 = np.array([1,1])
# ending_point1 = np.array([1000000000000,1])


# starting_point2 = np.array([0,0])
# ending_point2 = np.array([5, 5])

# print(Intersect(starting_point1,ending_point1,starting_point2,ending_point2))

import numpy as np
point_x = [0,20]
polygon_points = [[-10, 30], [10, 20], [15, 10], [-20, 10], [-10,30]]

def is_point_inside(polygon_points, point_x):
    count = 0
    point_y = [100000,point_x[0]]
    for i in range(len(polygon_points)-1):
        if Intersect(polygon_points[i],polygon_points[i+1],point_x,point_y) == "Intersecting" or PointsOnLineSegment(polygon_points[i],point_x,polygon_points[i+1]):
            print(polygon_points[i],polygon_points[i+1])
            count += 1
    if count == 0:
        return "Not inside polygon"
    elif count % 2 == 0:
        return "Outside polygon"
    elif count % 2 != 0:
        return "Inside a polygon"

print(is_point_inside(polygon_points,point_x))

polygon2 = [[-10, 30], [10, 20], [14, 10], [-20, 10]]
polygon1 = [[-20, 20], [15, 25], [15, 15], [-20, 20],[-20, 25]]

def point_inside_two_polygons(polygon1, polygon2):
    count1 = 0
    count2 = 0
    # my_list = []

    for i in range(len(polygon1)-1):
        for j in range(len(polygon2)):

            point_x1 = polygon2[j]
            point_x2 = [1000000,polygon2[j][1]]

            point_y1 = polygon2[j]
            point_y2 = [-1000000,polygon2[j][1]]

            if Intersect(polygon1[i],polygon1[i+1],point_x1,point_x2) == "Intersecting" :
                # print("Point inside polygon : ",polygon2[j])
                # print(polygon1[i],polygon1[i+1],point_x1,point_x2)
                count1 +=1 
                print(count1)
                # if polygon2[j] not in polygon1 and polygon2[j] not in polygon2:
                #     my_list.append(polygon2[j])
                # count += 1

            if Intersect(polygon1[i],polygon1[i+1],point_y1,point_y2) == "Intersecting" :
                # print("Point inside polygon : ",polygon2[j])
                # print(polygon1[i],polygon1[i+1],point_x1,point_x2)
                count2 += 1
                print(count2)


            if count1== 1 and count2 == 1:
                print("-------",polygon2[j])
        count1= 0
        count2 = 0


    # if count == 0:
    #     return "Not inside polygon"
    # elif count % 2 == 0:
    #     return "Outside polygon"
    # elif count % 2 != 0:
    #     return r"Inside a polygon {}".format(my_list) 

print(point_inside_two_polygons(polygon1, polygon2))