#https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        end = intervals[0][1]
        print(f"end={end}")
        count = len(intervals) - 1
        for i in range(1, len(intervals)):
            print(f"end={intervals[i][0]}")
            if intervals[i][0] >= end:
                end = intervals[i][1]
                print(f"end={end}")
                count -= 1
        print(f"intervals to remove=", count)
        return count
        
    def is_partial_overlap(self, x, y):
        print(f"part_overlap {x[0]} < {y[1]} and {y[0]} < {x[1]} => {x[0] < y[1] and y[0] < x[1]} => {x},{y} ")
        return x[0] < y[1] and y[0] < x[1]

    def is_full_overlap(self, x, y):
        print(f"full_overlap {x[0]} < {y[0]} and {x[1]} < {y[1]} => {x[0] < y[0] and x[1] < y[1]} => {x},{y} ")
        return x[0] < y[0] and x[1] < y[1]

    def is_right_overlapping(self, x, y):
        print(f"left_overlap {x[0]} == {y[0]} and {y[1]} > {x[1]} => {x[0] == y[0] and y[1] > x[1]} => {x},{y} ")
        return x[0] == y[0] and y[1] > x[1]

    def is_left_overlapping(self, x, y):
        print(f"right_overlap {y[0]} > {x[0]} and {x[1]} == {y[1]} => {y[0] > x[0] and x[1] == y[1]} => {x},{y} ")
        return y[0] > x[0] and x[1] == y[1]

    def isoverlapping(self, x, y):
        return self.is_partial_overlap(x,y) or self.is_full_overlap(x,y) or \
               self.is_left_overlapping(x,y) or self.is_right_overlapping(x,y)



    def mergelists(self, x, y):
        return [min(x[0],y[0]), max(x[1], y[1])]
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #print(intervals)
        intervals.sort(key=lambda interval: interval[0])
        count = len(intervals)-1
        overlapcount=0
        prev = False
        for i in range(1, len(intervals)):
            ret = self.isoverlapping(intervals[i-1], intervals[i]) 
            if ret:
                overlapcount =+ 1
                count -= 1

        print(f"intervals to remove=", max(count,overlapcount))
        return count

            



intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
intervals = [[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]]
intervals = [[1,2],[1,3],[1,4]]


#Solution().is_full_overlap([3,4], [5,6])
#Solution().is_partial_overlap([3,4], [5,6])
Solution().eraseOverlapIntervals(intervals)
Solution().eraseOverlapIntervals1(intervals)

'''
        #print(intervals)
        #for list in intervals:
            #print(list)

        #prev = False
        #all = True

        ##print(f"comparing {x[0]} < {y[0]} and {y[1]} < {x[1]}")
        #return True if x[0] < y[0] and y[1] < x[1] else False 
        return self.is_partial_overlap(x, y) or \
               self.is_right_overlapping(x,y) or \
               self.is_left_overlapping(x,y) or \
               self.is_full_overlap(x, y)
        
'''