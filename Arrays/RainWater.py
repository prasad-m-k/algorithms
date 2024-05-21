#https://leetcode.com/problems/trapping-rain-water

'''
we can simply do a pass from left to right, and then a pass from right to left, in order to calculate the largest known height so far in each direction. This saves memory as we store a constant amount of data (two values) for each input height instead of maintaining a separate data structure.

Time complexity: O(n) - Building the known maximums requires a loop in each direction, and iterating over the heights requires a single loop as the leftwards-largest and rightwards-largest are found in O(1) time.

Space complexity: O(1) - We store the known leftwards maximum and rightwards maximum, and keep track of the result as we go.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        height = [[0, 0, h] for h in height]
        max_left = 0
        max_right = 0
        for i in range(len(height)):
            height[i][0] = max_left
            max_left = max(max_left, height[i][2])
            height[~i][1] = max_right
            max_right = max(max_right, height[~i][2])
        result = 0
        for i in range(len(height)):
            result += max(0, min(height[i][0], height[i][1]) - height[i][2])
            max_left = max(max_left, height[i][2])
        return result
    
    #Working
    def trap2(self, height: List[int]) -> int:
        water = [0] * len(height)
        for i in range(1,len(height)):
            max_left =  max(height[:i])
            max_right = max(height[i:])
            #print(max_left)
            #print(max_right)
            water[i]= min (max_left,max_right)-height[i] if  min (max_left,max_right)-height[i] >= 0 else 0
            #water[i]
        #print(water)

        return sum(water)
    