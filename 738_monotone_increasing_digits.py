
def monotone_increasing_digits(n: int) -> int:
    if n < 10:
        return n
    digits = list(int(_) for _ in str(n))
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            for j in range(i, len(digits)):
                digits[j] = 9
            digits[i - 1] -= 1
    return int(''.join(str(_) for _ in digits).lstrip('0'))

def main():
    tests = [
        10,
        1234,
        332,
        100
    ]
    for test in tests:
        print(monotone_increasing_digits(test))

if __name__ == '__main__':
    main()

"""
my solution matches most others in the discussion
"""