def kth_smallest(arr, k):
    # First, find the maximum element in the array
    max_element = max(arr)
    print(max_element) 
    # Create a dictionary to store the frequency of each 
    # element in the input array
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
 
    # Keep track of the cumulative frequency of elements 
    # in the input array
    count = 0
    for i in range(max_element + 1):
        print(i, end = ".")
        if i in freq:
            count += freq[i]
            if count >= k:
                # If we have seen k or more elements, 
                # return the current element
                return i
 
    return -1

def kth_smallest2(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
        
    
    maxkey = max(freq.keys())
    print(freq)
    count = 0
    for i in range(maxkey+1):
        if i in freq:
            count += freq[i]
            if count >= k:
                return i
    
    return -1

arr = [12, 3, 5, 7, 19]
k = 2
print("\nThe", k,"th smallest element is", kth_smallest(arr, k))
print("\nThe", k,"th smallest element is", kth_smallest2(arr, k))
            
        