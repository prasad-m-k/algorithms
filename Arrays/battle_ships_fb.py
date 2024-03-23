#https://www.metacareers.com/profile/coding_puzzles?puzzle=3641006936004915
#Battleships probability

from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here

  if R == 0 or C == 0:
      return 0.0
  total = 0
  for i in range(len(G)):
      total += G[i].count(1)
  
  return(float(total/(R * C)))

  


R = 2
C = 3
G = [[0, 0, 1],
     [1, 0, 1]]

R = 2
C = 2
G = [[1, 1],
     [1, 1]]

print(getHitProbability(R, C, G))