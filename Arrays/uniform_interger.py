#
'''
A positive integer is considered uniform if all of its digits are equal. For example,  222 is uniform, while 
223 is not.
A = 75
B = 300

Sample test case #1
A = 75
B = 300
Expected Return Value = 5
Sample test case #2
A = 1
B = 9
Expected Return Value = 9
Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
'''

def reverse_int(num):
    digit = num % 10
    tens = 1
    while (num >= 1):
        rem = num % 10
        if rem != digit:
            return 0, tens//10
        num = num // 10
        tens *= 10
    return 1, tens//10

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  if A < 0 or B < 0 or  A > B or A > 10 ** 12:
      return 0
  x="Total uniform numbers between [" + str(A) + " - " + str(B) + "]"
  count = 0
  while A <= B:
      print(A)
      d, tens=reverse_int(A)
      count += d
      A += tens+tens//10
  
  print(x, count)
  return count

def getUniformIntegerCountInInterval_with_ret_array(A: int, B: int) -> int:
  # Write your code here
  print("--------------------")
  if A < 0 or B < 0 or  A > B or A > 10 ** 12:
      return 0

  ret = []
  count = 0
  i = A
  while i < (B+1):
      d, tens=reverse_int(i)
      if d:
          ret.append(i)
      count += d
      if(tens > 1):
          #print(i, d, count, tens)
          #print(f"jumping {tens+tens//10}")
          i += tens+tens//10
          #print(i, d, count)
          continue
      i += 1
  
  print(f"Total uniform numbers between [{A}-{B}]", count, ret)
  return count


getUniformIntegerCountInInterval(75,300)
exit(0)
#getUniformIntegerCountInInterval(1,1)
getUniformIntegerCountInInterval(1,9)
#getUniformIntegerCountInInterval(0,9)
#getUniformIntegerCountInInterval(10,10)
#getUniformIntegerCountInInterval(10,12)
getUniformIntegerCountInInterval(11,33)
getUniformIntegerCountInInterval(110,340)

#getUniformIntegerCountInInterval(550,666)
#getUniformIntegerCountInInterval(99,100)
#getUniformIntegerCountInInterval(75,100)

getUniformIntegerCountInInterval(9999999999,999999999999)
#getUniformIntegerCountInInterval(999999999999,999999999999)



