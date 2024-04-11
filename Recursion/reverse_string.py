

def reverse(s):
    if not len(s):
        return
    
    x = s[0]
    reverse(s[1:])
    print(x, end='')
    

reverse("Prasad MK")