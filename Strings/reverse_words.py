
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

        '''
        stack=[]
        word=""
        for i in range(len(s)):
            if s[i] == " ":
                if len(word):
                    stack.append(word)
                    word=""
                continue
            else:
                word+=s[i]
        if len(word):
            stack.append(word)
            word=""

        print(stack)
        s2 = ' '.join(stack[::-1])
        print(s2)
        return (s1)
        '''        
    

s=" the sky is blue "
#s="the sky is blue"
print(Solution().reverseWords(s))