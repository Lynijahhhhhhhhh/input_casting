# The distance from one point to another on a 2 Dimensional Plane is defined by the following equation:
#
#   d = sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)
#       where d = distance; sqrt() represent square root, or to the power of (1/2)

# Write a program that accepts two coordinates from the user and then calculates distance between the points.
# Example Output:
#   x1 = 5
#   y1 = 10
#
#   x2 = 35
#   y2 = -85
#
#   distance from (5, 10) to (35, -85) is 99.6423
def distance(x1,y1,x2,y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    #ITTTT WORKSSSSSSSSSSSSSSSSSSSSS
    print("distance from (",x1,",",y1,") to (",x2,",",y2,") is" , d)

from1=int(input("What is x1? "))
from2=int(input("What is y1? "))
to1=int(input("What is x2? "))
to2=int(input("What is y2? "))
distance(from1,from2,to1,to2)
