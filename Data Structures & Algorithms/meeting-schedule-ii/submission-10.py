"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        nums=1
        intervals.sort(key=lambda x:x.start)
        A=[intervals[0].end]
        for i in range(1,len(intervals)):
            if intervals[i].start>=A[0]:
                heapq.heappop(A)
                heapq.heappush(A,intervals[i].end)
            else:
                nums+=1
                heapq.heappush(A,intervals[i].end)
        return nums
        