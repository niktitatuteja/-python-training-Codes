class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        lis = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                lis.append(i)
                if len(lis) > 2:
                    return False

        if len(lis) != 2:
            return False

        i, j = lis
        return s1[i] == s2[j] and s1[j] == s2[i]