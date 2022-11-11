def check_distances(s, distance):
    letters = set(s)
    for letter in letters:
        first = s.find(letter)
        second = s[first+1:].find(letter)
        if second != distance[ord(letter) - 97]:
            return False
    return True


def main():
    tests = [
        ('abaccb', [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        ('aa', [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    ]
    for test in tests:
        print(check_distances(*test))


if __name__ == '__main__':
    main()


"""
instead of finding the second occurrence in the string,
you can directly check the value at firstindex + distance

def check_distances(s, distance):
    letters = set(s)
    for letter in letters:
        first = s.find(letter)
        dist = distance[ord(letter) - 97]
        if first + dist > len(s) - 1 or s[first + dist] != letter:
            return False
    return True
"""