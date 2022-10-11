

def max_score(s):
    return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))


def main():
    print(max_score('00111'))
    print(max_score('1111'))


if __name__ == '__main__':
    main()


"""
can also do a linear scan

def solution(s):
	zeros = 1 if s[0] == '0' else 0
	ones = s.count('1', 1)  # count 1s in s[1:]
	score = zeros + ones
	for i in xrange(1, len(s) - 1):
		if s[i] == '0':
			zeros += 1
		else:
			ones -= 1
		score = max(zeros + ones,  score)
	return score


"""