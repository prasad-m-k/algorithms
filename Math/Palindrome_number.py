#https://leetcode.com/problems/palindrome-number/description/

import math

def is_palindrome(x):
  if x == 0:
    return True
  k = int(math.log10(x))
  divisor = 10**k
  while x > 0:
    first_digit = x // divisor
    last_digit = x % 10
    if first_digit != last_digit:
      return False
    x = x % divisor
    x = x // 10
    divisor /= 100
  return True

print (is_palindrome(121))
#print (is_palindrome(1234321))
#print (is_palindrome(33))