#https://leetcode.com/problems/longest-common-prefix/
from typing import List
from time import time
from functools import reduce

def timer_func(func): 
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func


class Solution:
    @timer_func
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret=""
        min_len= len(reduce(lambda x,y: x if len(x) < len(y) else y, strs))
        print(min_len)
        list_len = len(strs)
        for c in range(list_len):
            for i in range(min_len):
                print(strs[i][c])
            
            ret += 
            break

        return ret
    
    
        


strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]

print(Solution().longestCommonPrefix(strs))
        