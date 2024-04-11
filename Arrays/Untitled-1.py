

def is_pal_rec(string):
    print(string)
    if len(string)<=1:
        return True

    if not string[1].isalpha():
        return is_pal_rec(string[2:])
    if not string[len(string)-1].isalpha():
        return is_pal_rec(string[:len(string)-1])
    
    if len(string)==2:
        return string[0] == string[1]

    return is_pal_rec(string[1:len(string)-1])

#is_pal_rec("malayalam1!")
is_pal_rec("racecar")
#print(is_pal_rec("racecar"))
#print(is_pal_rec("malayalam1!"))
#print(is_pal_rec("abac"))
#print(is_pal_rec("ab ba"))