from functools import reduce

arr=[1,2,2,2,4]

prod = reduce(lambda x, y: x * y, arr)
#print(prod)
prod_arr=[]

for x in arr:
    prod_arr.append(prod//x)
    #print(f"{prod} // {x} = {prod // x}")
 
print(prod_arr)

print( list(lambda x, y: x * y, arr) )