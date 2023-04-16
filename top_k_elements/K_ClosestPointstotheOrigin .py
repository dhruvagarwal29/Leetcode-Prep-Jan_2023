import heapq

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def eucledian_distance(self):
        return self.a*self.a + self.b*self.b

    # using max heap 
    def __lt__(self, other):
        return self.eucledian_distance() > other.eucledian_distance()

    # print point 

    def __str__(self) -> str:
        return f"[{self.a, self.b}]"


# using the point class we are going to solve this problem 
def find_closest_points(points, k):
    for i in points:
        print(i)
    maxHeap = []    
    # making the max heap of the points till k
    for i in range(k):
        heapq.heappush(maxHeap, points[i])
    
    # now go through the remaining points from the points list 
    # now if the coming point is closer to origin than the present point in heap,
    # remove the top point from heap and insert the current point in heap

    for i in range(k,len(points)):
        if points[i].eucledian_distance() < maxHeap[0].eucledian_distance():
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, points[i])

    return maxHeap



if __name__ == "__main__":
    points = [Point(1,3), Point(3,4), Point(2,-1)]
    k = 2

    result = find_closest_points(points,k)

    for res in result:
        print(res)