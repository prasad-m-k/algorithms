def isPalindrome1( s: str) -> bool:
    x=''.join([c.lower() for c in s if c.isalnum()])
    print(x)
    return x==x[::-1]
    
def isPalindrome(s):
    
    print(s)
    if len(s)<=1:
        return True

    L, R = 0, len(s)-1
    while(not s[L].isalnum()):
        print(f"\"{s[L]}\" is not alnum")
        L += 1
    while(not s[R].isalnum()):
        print(f"\"{s[R]}\" is not alnum")
        R -= 1


    return (s[L].lower() == s[R].lower()) and isPalindrome(s[L+1:R-1])

print(isPalindrome("malayalam!"))
#x=isPalindrome("A man, a plan, a canal: Panama")
#x=isPalindrome("race a car")
#x=isPalindrome(" ")
x=isPalindrome(",; W;:GlG:;l ;,")
print(x)
x=isPalindrome1(",; W;:GlG:;l ;,")
print(x)
#print(isPalindrome("racecar"))
#print(isPalindrome("malayalam1!"))
#print(isPalindrome("abac"))
#print(isPalindrome("ab ba"))

'''
if not s[0].isalnum():
    print(f"\"{s[0]}\" is not alnum")
    return isPalindrome(s[1:])
if not s[len(s)-1].isalnum():
    return isPalindrome(s[:len(s)-1])
'''
