#https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)-1
        intervals.sort(key=lambda interval:interval[1])
        
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            print(f"checking if {intervals[i][0]} >= {end}")
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count -= 1
        
        print(f"{intervals} remove = {count}")
        return count    



intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,3],[1,4]]
intervals = [[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]]
intervals = [[1,100],[11,22],[1,11],[2,12]]


Solution().eraseOverlapIntervals(intervals)

#Solution().is_full_overlap([3,4], [5,6])
#Solution().is_partial_overlap([3,4], [5,6])
#Solution().eraseOverlapIntervals1(intervals)

