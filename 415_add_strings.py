# You must solve the problem without using any built-in library 
# for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.


import itertools

def add(num1, num2):
    carry = '0'
    result_string = ''
    for n1, n2 in itertools.zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
        s = str(int(n1) + int(n2) + int(carry))
        carry = s[0] if len(s) > 1 else '0'
        result_string = s[-1] + result_string
    if carry != '0':
        result_string = carry + result_string
    return result_string




def main():
    print(add('213', '222'))
    print(add('919', '222'))
    print(add('1', '9'))

if __name__ == '__main__':
    main()


"""
Runtime: 90 ms, faster than 26.61% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 88.59% of Python3 online submissions for Add Strings.

my understanding of rule2 in the description was that you coulnt directly convert
the full input number into an int, but you could convert its digits individually
other ways to convert would be a dictionary
num_dict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
or using ordinal conversion and subtracting base ord(0)

some of the answers i see in the discussion end up converting the full numbers
to ints without int() and then adding the results once, but i don't like that

other answers are similar to mine, but do some shenanigans to accomplish line11
"""