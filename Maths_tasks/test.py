points = [[1,1],[1,-1],[-1,-1],[-1,1],[2,1],[1,2]]
angles = []
import math
for index in range(len(points)):
    starting_point = points[0]
    theta = math.degrees(math.atan2((points[index][1] - starting_point[1]),(points[index][0] - starting_point[0])))
    angles.append(theta)
print(angles)