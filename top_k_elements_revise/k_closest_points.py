# given an array of points of 2D plane, find 'K' closes points to origin

# here I have to make a class of points 
from heapq import *
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def eucledian_distance(self):
        # calculting the distance 
        return (self.x * self.x) + (self.y * self.y) 
    
    # for checking the which point is closer
    # for maxheap
    def __lt__(self,other): # it is using to fill maxheap using the > sign 
        return self.eucledian_distance() > other.eucledian_distance()

    # print the point
    
    def __str__(self) -> str:
        return f"[{self.x} , {self.y}]"
    
def find_closest_point(points, k):

    maxheap = [] # the __lt__ fucntion is working as maxheap

    for i in range(k):
        heappush(maxheap, points[i])

    for i in range(k,len(points)):
        if points[i].eucledian_distance() < maxheap[0].eucledian_distance():
            heappop(maxheap)
            heappush(maxheap, points[i])
    
    return maxheap

    

if __name__=="__main__":
    points = [Point(1,3), Point(3,4), Point(2,-1)]
    k = 2

    result = find_closest_point(points,k)

    for res in result:
        print(res)

