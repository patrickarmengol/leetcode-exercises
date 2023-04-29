class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        class kmap(dict):
            def __missing__(self, key):
                return "?"

        return s.replace("(", "{").replace(")", "}").format_map(kmap(knowledge))


s = Solution()
print(s.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(s.evaluate("hello(name)", [["a", "b"]]))
print(s.evaluate("(a)(a)(a)aaa", [["a", "yes"]]))
