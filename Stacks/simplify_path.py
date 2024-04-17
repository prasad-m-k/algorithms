#https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        #def removepath(path):
        print(path)
        stack = []
        for subpath in path.split("/"):
            if subpath == "..":
                if stack:
                    stack.pop()
            elif subpath == "." or not subpath:
                continue
            else:
                stack.append(subpath)
        
        print("/".join(stack))
        return "/"+"/".join(stack)
       

path = "/home/"
path = "/../"

path = ""
path = "/a/./b/../../c/"

path = "/.."
path = "/home//test/"
print(Solution().simplifyPath(path))
 