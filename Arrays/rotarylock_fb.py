#https://www.metacareers.com/profile/coding_puzzles?puzzle=990060915068194

from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
    time = 0
    C.insert(0, 1)
    ind = 1
    while (ind < M+1):
        fwd = (C[ind] - C[ind-1]) % N
        rev = (C[ind-1] - C[ind]) % N
        #print(f"fwd={fwd}, rev={rev}")
        time += min( fwd, rev)
        ind += 1

    print(f"ans2={time} sec.")
    return time



N = 10
M = 4
C = [9, 4, 4, 8]
getMinCodeEntryTime(N, len(C), C)

C = [9, 10, 5, 9]
getMinCodeEntryTime(N, len(C), C)


N = 10
M = 3
C = [10, 3, 2]
getMinCodeEntryTime(N, len(C), C)


