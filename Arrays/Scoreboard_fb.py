#https://www.metacareers.com/profile/coding_puzzles?puzzle=348371419980095
#Scoreboard Inference

from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  ret = max(S) // 2
  if any(n % 2 == 1 for n in S):
    ret += 1
  print(f"ret1={ret}, => S={S}")
  return ret


S = [3,2,3]
S = [2, 4, 6, 8]
S = [1, 3, 2, 4, 5, 6]
S = [5,5,5]

getMinProblemCount(len(S), S)

S = [2,2,1]
getMinProblemCount(len(S), S)

S = [3, 2, 3, 1]
getMinProblemCount(len(S), S)

S = [3, 3, 3]
getMinProblemCount(len(S), S)

S = [ 1, 2 ]
getMinProblemCount(len(S), S)


S = [ 1, 2, 3 ]
getMinProblemCount(len(S), S)

S = [1, 3, 2, 4, 5, 6]
getMinProblemCount(len(S), S)

S = [4, 3, 3, 4]
getMinProblemCount(len(S), S)

S = [2, 4, 6, 8]
getMinProblemCount(len(S), S)

S = [1,1,1,2]
getMinProblemCount(len(S), S)


S = [ 2 ]
getMinProblemCount(len(S), S)

S = [1, 1]
getMinProblemCount(len(S), S)
