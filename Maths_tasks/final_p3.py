
#============================================== program-3 ==========================================

import numpy as np
np.seterr(divide='ignore', invalid='ignore')
polygon1 = [[-10, 30], [10, 20], [15, 10], [-20, 10],[-10, 30]]
polygon2 = [[-20, 25], [15, 25], [15, 15], [-20, 20],[-20, 25]]

# polygon1 = [[-1, 1], [4,4], [2,3], [-1,1]]
# polygon2 = [[4.5,4.5], [6,6], [5,6], [4.5,4.5]]

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
            s = q2-p2
            try:
                t = np.cross((p2 - p1),s)/np.cross(r,s)
                u = np.cross((p1-p2),r)/np.cross(s,r)

                t0 = np.dot((p2-p1),r)/np.dot(r,r)
                t1 = np.dot((p2 + s - p1),r)/np.dot(r,r)
            
                # print("t0---- ",t0)
                # print("t1---- ",t1)
            except Exception as e:
                    # print(e)
                    pass
            else:
                if np.cross(r,s) != 0 and t >= 0 and t <= 1 and u >= 0 and u <= 1:
                    # print("Line segments are intersecting at points: ",p1 + t*r)
                    point = p1 + t*r
                    if list(point) not in intersecting_points:
                        intersecting_points.append(list(point))

                if np.cross(r,s) == 0 and np.cross((p2-p1),r) == 0 :
                    if (t0<=1 and t0 >=0) or (t1<=1 and t1 >=0) :
                        print("Lines are colinear and overlapping")
                        # print(q2,q1)
                        if ((p2[0]>=p1[0] and p2[0] <= q1[0]) or (p2[0]<=p1[0] and p2[0] >= q1[0])) and ((p2[1]>=p1[1] and p2[1] <= q1[1]) or (p2[1]<=p1[1] and p2[1] >= q1[1])):
                            print("Overlapping point : ",p2)
                            if list(p2) not in intersecting_points:
                                intersecting_points.append(list(p2))

                        if ((q2[0]>=p1[0] and q2[0] <= q1[0]) or (q2[0]<=p1[0] and q2[0] >= q1[0])) and ((q2[1]>=p1[1] and q2[1] <= q1[1]) or (q2[1]<=p1[1] and q2[1] >= q1[1])):
                            print("Overlapping point : ",q2)
                            if list(q2) not in intersecting_points:
                                intersecting_points.append(list(q2))

                        if ((q1[0]>=p2[0] and q1[0] <= q2[0]) or (q1[0]<=p2[0] and q1[0] >= q2[0])) and ((q1[1]>=p2[1] and q1[1] <= q2[1]) or (q1[1]<=p2[1] and q1[1] >= q2[1])):
                            print("Overlapping point : ",q1)
                            if list(q1) not in intersecting_points:
                                intersecting_points.append(list(q1))

                        if ((p1[0]>=p2[0] and p1[0] <= q2[0]) or (p1[0]<=p2[0] and p1[0] >= q2[0])) and ((p1[1]>=p2[1] and p1[1] <= q2[1]) or (p1[1]<=p2[1] and p1[1] >= q2[1])):
                            print("Overlapping point : ",p1)
                            if list(p1) not in intersecting_points:
                                intersecting_points.append(list(p1))
                    else :
                            # print("Lines are colinear and disjoint")
                            pass

                if np.cross(r,s) == 0 and np.cross((p2-p1),r) != 0:
                    # print("two lines are parallel and non-intersecting.")
                    pass
            

        line.clear()
            
if len(intersecting_points) == 0:
    print("No points are intersecting")
else:
    print("Intersecting points are : \n",intersecting_points)