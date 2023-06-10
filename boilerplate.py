class Solution:
    def some_function(self, a):
        if a == "input":
            return "output"
        else:
            return "nope"


tests = [
    (
        "input",
        "output",
    ),
    (
        "put",
        "output",
    ),
]


def test_sol():
    s = Solution()
    for i, test in enumerate(tests, 1):
        print(f"\ntest #{i} \nin:  {test[0]}\nout: {test[1]}")
        assert s.some_function(test[0]) == test[1]
