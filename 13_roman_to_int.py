def roman_to_int(s):
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    
    total = 0
    i = 0
    while i < len(s):
        x = s[i]
        if x in 'IXC' and i+1 < len(s) and s[i:i+2] in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            x = s[i:i+2]
            i += 2
        else:
            i += 1
        total += d[x]
    return total



for test in ['III', 'LVIII', 'MCMXCIV', 'XVII', 'XIV', 'CDXIII']:
    print(roman_to_int(test))



"""
nice solution i found in comments
iterate backwards and keep track of prev to determine whether to subtract

def romanToInt(self, s):
    _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev = 0
    sum = 0
    for i in s[::-1]:
        curr = _dict[i]
        if prev > curr:
            sum -= curr
        else:
            sum += curr
        prev = curr
    return sum
"""