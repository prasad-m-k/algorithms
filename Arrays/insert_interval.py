#https://leetcode.com/problems/insert-interval/
from typing import List

class Solution:
    def merge(self, x, y):
        return [min(x[0],y[0]), max(x[1], y[1])]

    def islater(self, x, y): #if x is later than y
        return (x[0] > y[1])

    def isprev(self, x, y): #if x is later than y
        return (x[1] < y[0])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals
        
        res = []
        for i,interval in enumerate(intervals):
            if self.isprev(newInterval, interval): 
                res.append(newInterval)
                return res + intervals[i:]
            elif self.islater( newInterval, interval): 
                res.append(interval)
            else: 
                newInterval = (self.merge(newInterval,interval))
                
        res.append(newInterval)
        
        return res
class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        print(f"{intervals}, {newInterval}")
        ilen=len(intervals)
        if ilen == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals
        

        def overlap(x,y):
            return x[0] <= y[1] and y[0] <= x[1]

        def merge(x,y):
            return [min(x[0],y[0]), max(x[1],y[1])]
        
        def updateret(x,y):
            if(overlap(x, y)):
                ret[-1] = merge(x, y)
            else:
                ret.append(y)
        
        ret = [intervals[0]]
        inserted = False
        i=0

        #for i in range(0, ilen):
        while i < ilen:
            print(f"working on  = {intervals[i]}")
            if not inserted and overlap(ret[-1], newInterval):
                ret[-1] = merge(ret[-1], newInterval)
                inserted = True
            else:
                if not inserted:
                    if newInterval[[0][0]] < ret[-1][0]:
                        ret.insert(i, newInterval)
                        inserted = True
                    elif newInterval[[0][0]] < intervals[i][0]:
                        ret.insert(i, newInterval)
                        inserted = True
            
            updateret(ret[-1], intervals[i])
            i += 1
        if not inserted:
            updateret(ret[-1], newInterval)
            
        print(f"return {ret}")
        return ret
    
    
    

intervals = [[1,5]]
newInterval = [2,3]
intervals = []
intervals = [[1,3],[6,9]]
newInterval = [2,5]


newInterval = [0,0]

intervals = [[1,3],[6,8],[9,9]]
newInterval = [7,8]

intervals = [[3,5],[12,15]]
newInterval = [6,6]


intervals = [[1,5]]
newInterval = [6,8]


intervals = [[0,2],[3,5],[6,8],[10,12],[13,15]]
newInterval = [4,7]


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]


print(Solution().insert(intervals, newInterval))

            #if not inserted and overlap(newInterval, ret[-1]):
            #    ret[-1] = merge(newInterval, ret[-1])
            #    inserted = True
