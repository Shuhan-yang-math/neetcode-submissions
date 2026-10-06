class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        i=0
        n=len(intervals)
        start,end=newInterval
        while i<n and intervals[i][1]<start:
            result.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=end:
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            i+=1
        result.append([start,end])
        result.extend(intervals[i:])
        return result
        
        