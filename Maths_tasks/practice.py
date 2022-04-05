import numpy as np
p1 = np.array([1,2])
q1 = np.array([6,4])
p2 = np.array([3,5])
q2 = np.array([8,1])

# orientation for non colinear points--------------------

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

print(Intersect(p1,q1,p2,q2)) 