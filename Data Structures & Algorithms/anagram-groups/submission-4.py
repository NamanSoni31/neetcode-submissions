class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = []
        d = {}
        for i in range(len(strs)):
            x = sorted(strs[i])
            if strs[i] in d:
                continue
            lst = [strs[i]]
            for j in range(i+1, len(strs), 1):
                if len(strs[j]) != len(strs[i]):
                    continue
                y = sorted(strs[j])
                value = True
                for w in range(len(x)):
                    if x[w] != y[w]:
                        value = False
                if value: 
                    lst.append(strs[j])
                    d[strs[j]] = j
            groupings.append(lst)
        print(d)
        return groupings