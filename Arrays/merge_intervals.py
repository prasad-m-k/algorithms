from typing import List

class Solution:
    def is_overlap(self, x, y):
        #if x[0] <= y[1] and y[0] <= x[1]:
        if  y[0] <= x[1]:            
            print(f"{x} and {y} intervals overlap")
            return True
        return False

    def merge_items(self, x, y):
        return [min(x[0],y[0]), max(x[1],y[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #print(intervals)
        intervals.sort(key=lambda interval: interval[0])
        print(intervals)
        interval_len=len(intervals)
        i= 0
        ret = [intervals[0]]
        
        #ret.append(intervals[0])
        print(f"initial ret={ret}")
        while i < interval_len-1:
            if  self.is_overlap(ret[-1], intervals[i+1]):
                ret[-1]=self.merge_items(ret[-1], intervals[i+1])
            else:
                ret.append(intervals[i+1])
            i += 1

            
        print(f"ret={ret}")
        return ret
        

intervals = [[1,4],[0,2],[3,5]]
intervals = [[2,6],[3,4]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

Solution().merge(intervals)