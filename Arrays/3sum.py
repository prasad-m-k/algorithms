class Solution(object):
  def threeSum(self, nums):
    results = []
    nums.sort()
    print(nums)
    length = len(nums)
    # Range is length - 2 because we need at least
    # 3 numbers to continue
    print(nums[0:length - 2])
    for i in range(length - 2):
      # The sum of 3 positive numbers will always be > 0.
      if nums[i] > 0:
        break
      # If nums[i] == nums[i - 1], it's a duplicate
      # element and we don't need to check.
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      l, r = i + 1, length - 1
      while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total < 0:
          l += 1
        elif total > 0:
          r -= 1
        else:
          results.append([nums[i], nums[l], nums[r]])
          while l < r and nums[l] == nums[l + 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          l += 1
          r -= 1
    return results


nums = [-5, 5, 1, -1, 1, -2, 2, 0]
print(Solution().threeSum(nums))