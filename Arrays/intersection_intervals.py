from typing import List

class Solution:
    
    def intersection(self, x,y):
        if (x[1] >= y[0]) and (x[0] <= y[1]):
            return [max(x[0],y[0]), min(x[1], y[1])]
        else:
            return None
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        print(self.intersection([0,2],[8,10]))
        merged=[]
        for x in firstList:
            for y in secondList:
                i = self.intersection(x, y)
                if i:
                    merged.append(i)
        
        return (merged)
        
        


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

firstList = [[1,3],[5,9]]
secondList = []
print(Solution().intervalIntersection(firstList, secondList))



"""_summary_
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].    
"""
