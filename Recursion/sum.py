

def arrsum (arr, Sum):
    N = len(arr)
    if N == 0:
        return Sum
    
    return arrsum(arr[:N-1], Sum + arr[N-1])


print(arrsum([1,2,3,7,8,10], 0))