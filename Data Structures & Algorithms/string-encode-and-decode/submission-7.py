class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for elem in strs:
            length = len(elem)
            encoded = f"{encoded}{length}~{elem}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "~":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            
            i = j + 1 + length
            j = i
        return res