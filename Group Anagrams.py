import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            ans[sorted_s].append(s)

        return list(ans.values())