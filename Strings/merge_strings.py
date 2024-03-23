#https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        l=max(l1,len(word2))
        ret=""
        for i in range(0,l):
            if i >= l2:
                ret+=word1[i:l1]
                break
            if i >= l1:
                ret+=word2[i:l2]
                break
            ret+=word1[i]
            ret+=word2[i]



        print(ret)
        

word1 = "abc"
word2 = "pqr"
Solution().mergeAlternately(word1, word2)


word1 = "ab"
word2 = "pqrs"
      
Solution().mergeAlternately(word1, word2)
word1 = "abcd"
word2 = "pq"
Solution().mergeAlternately(word1, word2)