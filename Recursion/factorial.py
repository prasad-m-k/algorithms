
memo={}

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    if num in memo:
        return memo[num]
    
    memo[num] = num * factorial(num-1)
     
    #print(memo)
    return memo[num]

print(factorial(7))