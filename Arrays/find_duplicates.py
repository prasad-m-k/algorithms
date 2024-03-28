

def has_duplicates(nums) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True

def has_duplicates2(nums) -> bool:
    for i in nums:
        if nums.count(i) > 0:
            return True
    
    return False


nums=[1,2,1]
print(has_duplicates(nums))
print(has_duplicates2(nums))