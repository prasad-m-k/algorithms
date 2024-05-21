class Solution:
    def decodeString(self, s: str) -> str:
        i, digit, size = 0, 0, len(s)
        decoded=""
        while (i < len(s)):
            if s[i].isdigit():
                digit=digit*10+int(s[i])
                i+=1
                continue
            else:
                if s[i] == "[":
                    start = i
                    
                    nstart = s.index('[',start+1)
                    end = s.index(']',start+1)
                    print("s=",s ,"substring=", s[start+1:end])
                    if nstart < end:
                        decoded += self.decodeString(digit*s[start+1:end+1])
                    else:
                        decoded  += digit*s[start+1:end]
                        i=end
                    digit=0
                    
                else:
                    decoded+=s[i]
            i+=1
        print("return=", decoded)
        return decoded


s="3[a2[c]]"
print(Solution().decodeString(s))

s = "3[a]2[bc]"
#print(Solution().decodeString(s))

s = "2[abc]3[cd]ef"
#print(Solution().decodeString(s))