import math
class Point:
    __x = 0.0
    __y = 0.0

    def __init__(self, x = None, y = None):
        if (x != None and y != None):
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0
    
    # Since its private varaible, we need to use getter.
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # Use known-distance
    def distance(self, otherPoint):
        dist = math.sqrt(pow((self.__x - otherPoint.getX()), 2) + pow((self.__y - otherPoint.getY()), 2))
        return dist
    
    # Add Two point and return new point
    def __add__(self, otherPoint):
        new_x = self.__x + otherPoint.getX()
        new_y = self.__y + otherPoint.getY()
        return Point(new_x, new_y)


# Example - Same Point
p1 = Point(1, 1)
p2 = Point(2, 2)
dist = p1.distance(p2)
print("Distance: ", dist)

p3 = p1 + p2
print("New P3 Point: (", p3.getX(), ",", p3.getY(), ")")