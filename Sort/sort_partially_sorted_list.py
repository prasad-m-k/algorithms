import heapq
def sort_partially_sorted(nums, k):
  h = []
  sorted = []
  k += 1
  # Create sliding window
  for n in nums[:k]:
    heapq.heappush(h, n)


  for n in nums[k:]:
    sorted.append(heapq.heapreplace(h, n))


  while len(h) > 0:
    sorted.append(heapq.heappop(h))

  return sorted
  

print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]
