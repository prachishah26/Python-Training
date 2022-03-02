# Find the overlapping area of two rectangles
# Rectangles can be in any direction

a = [1,1]
b = [4,4]
c = [2,2]
d = [6,6]
x = 0
y = 1
x_distance = min(b[x],d[x]) - max(a[x],c[x])
y_distance = min(b[y],d[y]) - max(a[y],c[y])
area = 0
if x_distance>0 and y_distance>0:
    area = x_distance*y_distance
print(area)