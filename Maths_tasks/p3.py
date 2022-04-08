import numpy as np

p1 = np.array([10,20])
q1 = np.array([15,10])
p2 = np.array([20,10])
q2 = np.array([-10,10])

# if ( (p2[0] <= max(p1[0], other_point[0])) and (q[0] >= min(p[0], other_point[0])) and
# 		(q[1] <= max(p[1], other_point[1])) and (q[1] >= min(p[1], other_point[1]))):

if ((p2[0]>=p1[0] and p2[0] <= q1[0]) or (p2[0]<=p1[0] and p2[0] >= q1[0])) and ((p2[1]>=p1[1] and p2[1] <= q1[1]) or (p2[1]<=p1[1] and p2[1] >= q1[1])):
    print(p2)
if ((q2[0]>=p1[0] and q2[0] <= q1[0]) or (q2[0]<=p1[0] and q2[0] >= q1[0])) and ((q2[1]>=p1[1] and q2[1] <= q1[1]) or (q2[1]<=p1[1] and q2[1] >= q1[1])):
    print(q2)
if ((q1[0]>=p2[0] and q1[0] <= q2[0]) or (q1[0]<=p2[0] and q1[0] >= q2[0])) and ((q1[1]>=p2[1] and q1[1] <= q2[1]) or (q1[1]<=p2[1] and q1[1] >= q2[1])):
    print(q1)
if ((p1[0]>=p2[0] and p1[0] <= q2[0]) or (p1[0]<=p2[0] and p1[0] >= q2[0])) and ((p1[1]>=p2[1] and p1[1] <= q2[1]) or (p1[1]<=p2[1] and p1[1] >= q2[1])):
    print(p1)