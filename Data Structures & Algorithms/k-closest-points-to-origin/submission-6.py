class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i]=[points[i][0],points[i][1],points[i][0]*points[i][0]+points[i][1]*points[i][1]]
        points.sort(key=lambda x:x[2])
        b=[i[0:2] for i in points]
        return b[0:k]
        