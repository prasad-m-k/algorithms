from typing import List
from math import factorial

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        print("Using nCr Formula i.e. n!/(n-r)!r! n!/(n-r)!r! ")

        #rows = int(input("Please enter the number of rows (upto 5 only) : "))
        res = []
        for i in range(numRows):
            #for j in range(numRows-i+1):
            #    print(end=" ")
            inner=[]
            for j in range(i+1):
                
                f = factorial(i)//(factorial(j)*factorial(i-j))
                print(f"n={i} r={j} f={f}")
                inner.append(f)
                #print(f, end=" ")
            print(inner)
            res.append(inner)
        
        print(res)
        return res
        res = []
        for r in range(numRows):
            print(' '*(numRows-r), end='')
            print(' '.join(map(str, str(11**r))))        
            res.append(list(map(int, str(11**r))))

        print(res)
        return res
        
Solution().generate(2)
Solution().generate(15)