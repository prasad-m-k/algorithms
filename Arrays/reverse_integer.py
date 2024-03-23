

rev = 0
ind = 1

def reverse1(x: int) -> int:
    rev = 0
    sign = -1 if x < 0 else 1
    x *= sign
    while(x):
        rev = (rev * 10) + (x % 10)
        x = x // 10

    ret = sign * (rev)
    return 0 if ret <= -2147483648 or ret >= 2147483647 else ret


def reverse(x: int) -> int:
    rev = 0
    sign = -1 if x < 0 else 1
    x *= sign
    while(x):
        dm=divmod(x,10)
        rev = (rev * 10) + dm[1]
        x = dm[0]

    ret = sign * (rev)
    return 0 if ret <= -2147483648 or ret >= 2147483647 else ret
    
'''
'''
print(reverse(5))
print(reverse(32))
print(reverse(567))
print(reverse(-123))
print(reverse(1534236469))