from vector import Vector
from line import Line
from plane import Plane

# print Vector([1,2,3])

plane_1 = Plane(normal_vector=Vector([-7.926,8.625,-7.217]), constant_term=-7.952)
plane_2 = Plane(normal_vector=Vector([-2.642,2.875,-2.40566666666]), constant_term=-2.443)

print plane_1.is_parallel(plane_2)
print plane_1 == plane_2

[1, 2, 0 | 3]
[0, 0, 0 | 0]
[0, 0, 1 | -4]

[x,y,z] = [3-2y, y, -4]
        = [3, 0, -4] + y[-2, 1, 0]


[1, 2, 0 | 3]
[0, 0, 1 | -4]
[0, 0, 0 | 0]