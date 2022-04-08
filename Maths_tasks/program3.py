# TASK 3:-------------------------------------------------

# Find area between 2 overlapping polygons (can be any type of polygon)
# polygon1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]
# polygon2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]


# ====================  step -1 checking if two line segments intercects or not ======================

import numpy as np
p1 = np.array([15,25])
q1 = np.array([15,15])
p2 = np.array([15,10])
q2 = np.array([100000,10])

# orientation for non colinear points---------------------

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
    if c == 0 and PointsOnLineSegment(p2,p1,q2) == 1:
        return "Intersecting"
    if c == 0 and PointsOnLineSegment(p2,q1,q2) == 1:
        return "Intersecting"
    if a != b and c != d:
        return "Intersecting"
    
    return "Not Intersecting"

print(Intersect(p1,q1,p2,q2)) 



# ============================  step - 2 finding intercecting poing  ===================================

# import numpy as np

# p1 = np.array([1,2])
# q1 = np.array([6,4])
# q2 = np.array([3,5])
# p2 = np.array([8,1])

# p1 = np.array([-20,20])
# q1 = np.array([15,15])
# q2 = np.array([-10,30])
# p2 = np.array([-20,10])

# p1 = np.array([-20,25])
# q1 = np.array([15,25])
# q2 = np.array([-10,30])
# p2 = np.array([-20,10])

# p1 = np.array([3,5])
# q1 = np.array([7,5])
# q2 = np.array([6,5])
# p2 = np.array([10,5])

# p1 = np.array([1,1])
# q1 = np.array([4,4])
# q2 = np.array([3,3])
# p2 = np.array([6,6])

# p1 = np.array([4,4])
# q1 = np.array([5,5])
# q2 = np.array([7,7])
# p2 = np.array([8,8])

# p1 = np.array([10,20])
# q1 = np.array([15,10])
# p2 = np.array([20,10])
# q2 = np.array([-10,10])

r = q1 - p1  #magnitude of vector
print(r)

s = q2-p2
print(s)

t = np.cross((p2 - p1),s)/np.cross(r,s)
u = np.cross((p1-p2),r)/np.cross(s,r)
print("t and u are : ",t,u)

print(p1 + t*r)
print(p2 + u*s)
t0 = np.dot((p2-p1),r)/np.dot(r,r)
t1 = np.dot((p2 + s - p1),r)/np.dot(r,r)
# print(t0-t1)
print(t0,t1)
if np.cross(r,s) == 0 and np.cross((p2-p1),r) == 0 :
    if t0<=1 and t0 >=0 and t1<=1 and t1 >=0 :
        print("Lines are colinear and overlapping")
        print(q2,q1)
    else :
        print("Lines are colinear and disjoint")

if np.cross(r,s) == 0 and np.cross((p2-p1),r) != 0:
    print("two lines are parallel and non-intersecting.")
if np.cross(r,s) != 0 and t >= 0 and t <= 1 and u >= 0 and u <= 1:
    print("Line segments are intersecting at points: ",p1 + t*r)
else:
    print("---")






    