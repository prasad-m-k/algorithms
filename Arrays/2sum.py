class Solution(object):
    def twosum(self, target, nums):
        ind_map={}

        for i, num in enumerate(nums):
            inv = target - num

            if inv in ind_map:
                return [ind_map[inv],i]

            ind_map[num] = i


print(Solution().twosum(9, [2,7,11,15]))