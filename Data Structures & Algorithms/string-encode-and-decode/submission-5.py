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
            word = s[j+1:j + 1 + length]
            res.append(word)
            print(word)
            i = j + 1 + length
            j = i
        return res