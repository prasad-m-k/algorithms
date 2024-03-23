#https://www.metacareers.com/profile/coding_puzzles?puzzle=203188678289677
#Social Distance

from typing import List
# Write any import statements here
from time import time
import math
import bisect


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  try:
      if N == 0 or K == 0 or M >= N:
        return 0
    
      if not S or M == 0:
        return N // (K+1)
      
      ret = 0
      guest = 0
      matrix = [0] * N
      S.sort()
      for s in S:
          matrix [s-1] = 1
    
      print(f"matrix={matrix}, S={S}")
      for i in range(0,N):
          rmin = 0 if (i-K) <= 0 else (i-K)
          rmax = N-1 if (i+K) >= N else (i+K)
          print(f"Range={rmin}:{rmax}, {S}")
          for x in range(rmin,rmax+1,K):
              if x not in S:#bisect.insort(S,i)
                  guest += 1
                  #print(x, end=" ,")
              #print("insert ?")
              
          if matrix[rmin:rmax+1].count(1) == 0:
              matrix[i] = 1
              
              ret += 1
              print(f"Range={rmin}:{rmax}, {S}")

      print("guest=", guest)
      return ret

  except:
      return 0
    

N = 15
K = 2
M = 3
S = [15,1,7]
#getMaxAdditionalDinersCount4(N, K, M, S)
print(getMaxAdditionalDinersCount(N, K, M, S))
#getMaxAdditionalDinersCount1(N, K, M, S)
exit(0)
getMaxAdditionalDinersCount(N, K, M, S)
#getMaxAdditionalDinersCount2(N, K, M, S)
#getMaxAdditionalDinersCount3(N, K, M, S)
#exit(0)

N = 10
K = 1
M = 2
S = [2, 6]
getMaxAdditionalDinersCount(N, K, M, S)
#getMaxAdditionalDinersCount2(N, K, M, S)
#getMaxAdditionalDinersCount3(N, K, M, S)

N = 15
K = 2
M = 3
S = [11, 6, 14]

getMaxAdditionalDinersCount(N, K, M, S)
#getMaxAdditionalDinersCount2(N, K, M, S)
#getMaxAdditionalDinersCount3(N, K, M, S)

N = 15
K = 1
M = 1
S = [1]

getMaxAdditionalDinersCount(N, K, M, S)
#getMaxAdditionalDinersCount2(N, K, M, S)
#getMaxAdditionalDinersCount3(N, K, M, S)

'''
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  num_new_diners = (S[0] - 1) // (K + 1)
  for i in range(1, len(S)):
    num_new_diners += (S[i] - S[i-1] - K-1) // (K + 1)
  num_new_diners += (N - S[-1]) // (K + 1)
  return num_new_diners
'''