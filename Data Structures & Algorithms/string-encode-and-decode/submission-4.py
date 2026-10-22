class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return "empty"
        result = ""
        for i, j in enumerate(strs):
            print("DD", j)
            if i >= len(strs) - 1:
                result += j
            else:
                result += j + "nm"
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "empty":
            return []
        return s.split("nm")
