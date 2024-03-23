# Check if a string is a palindrome in single liner, ignoring spaces, digits and special characters.

def is_palindrome(palstr: str) -> bool:
    
    if ''.join(c.lower() for c in palstr if c.isalpha()) == ''.join(c.lower() for c in palstr if c.isalpha())[::-1]:
        return True    
    
    return False
    

def main() -> None:
    palstr="Race car1!"
    print(f"{palstr}  is a Palindrome: {is_palindrome(palstr)}")

    palstr="#aba99baba"
    print(f"{palstr}  is a Palindrome: {is_palindrome(palstr)}")

    palstr="Prasad"
    print(f"{palstr} is a Palindrome: {is_palindrome(palstr)}")


if __name__ == "__main__":
    main()
