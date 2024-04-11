class Solution(object):
    def twosum(self, target, nums):
        summap={}
        for ind, num in enumerate(nums):
            inv = target - num
            if inv in summap:
                print(summap)
                return [summap[inv], ind]
            summap[num] = ind


    '''
    def twosum(self, target, nums):
        ind_map={}

        for i, num in enumerate(nums):
            inv = target - num

            if inv in ind_map:
                return [ind_map[inv],i]

            ind_map[num] = i
    '''

print(Solution().twosum(9, [2,7,11,15]))
print(Solution().twosum(6, [3,2,4]))