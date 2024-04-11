# Check if a string is a palindrome in single liner, ignoring spaces, digits and special characters.

def is_palindrome(palstr: str) -> bool:
    
    return True if ''.join(c.lower() for c in palstr if c.isalpha()) == \
           ''.join(c.lower() for c in palstr if c.isalpha())[::-1] else False
    

import itertools

#Using 2 pointers, sliding
def is_palindrome2(palstr: str) -> bool:
    i = 0
    rev = -1
    while i < len(palstr)-1 and rev >= (-1) * len(palstr):
        c1 = palstr[i]
        c2 = palstr[rev]
        while (not c1.isalpha()) and (i < len(palstr)-1) :
            i += 1
            c1 = palstr[i]
            
        while (not c2.isalpha()) and (rev > (-1) * len(palstr)+1) :
            rev -= 1
            c2 = palstr[rev]
        
        
        if c1.isalpha() and c2.isalpha() and c1.lower() != c2.lower():
            return False
        i += 1
        rev -= 1
        
    return True



def main() -> None:

    palstr="a11222333ab"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")

    palstr="11222333"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")

    palstr="#a#"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")
    print("------------------------------------")

    palstr="Race car1!"
    print(f"{palstr}  is a Palindrome: {is_palindrome(palstr)}")

    palstr="#aba99baba"
    print(f"{palstr}  is a Palindrome: {is_palindrome(palstr)}")

    palstr="Prasad"
    print(f"{palstr} is a Palindrome: {is_palindrome(palstr)}")

    print("------------------------------------")
    palstr="Race car1!"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")

    palstr="#aba99baba"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")

    palstr="Prasad"
    print(f"{palstr} is a Palindrome: {is_palindrome2(palstr)}")

    print("------------------------------------")
    palstr=""
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")

    palstr="76MalaY!23alam23"
    print(f"{palstr}  is a Palindrome: {is_palindrome2(palstr)}")



if __name__ == "__main__":
    main()