
def substrings_of_others(words):
    r = []
    s = sorted(words, key=len) # i thought sorting it first would improve runtime, but maybe not
    for i, w in enumerate(s):
        for o in s[i+1:]:
            if w in o:
                r.append(w)
                break # could do set instead
    return r

def main():
    print(substrings_of_others(["mass","as","hero","superhero"]))
    print(substrings_of_others(["leetcode","et","code"]))
    print(substrings_of_others(["leetcoder","leetcode","od","hamlet","am"]))

if __name__ == '__main__':
    main()

"""
Runtime: 73 ms, faster than 40.15% of Python3 online submissions for String Matching in an Array.
Memory Usage: 13.7 MB, less than 97.69% of Python3 online submissions for String Matching in an Array.

most python solutions in discussions were similar to mine
there was one with tries that i don't really want to touch
"""