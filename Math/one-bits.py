
def countones(num):
    count = 0
    while num > 0:
        print(num, end = " >> ")
        count += num & 1
        num >>= 1
        print(num)
    
    print(count)
    return count


countones(255)