def majority_element(nums):
    count = 0
    result = 0

    for num in nums:
        if count == 0:
            result = num

        if result == num:
            count += 1
        else:
            count -= 1

    return result


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
print(majority_element([3, 3, 3, 3, 3, 1, 1, 1, 2]))
