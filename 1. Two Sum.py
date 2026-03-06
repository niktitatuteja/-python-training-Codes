class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        m = {}

        for val in nums:
            result = target - val
            if result in m:
                return [m[result], index]
            m[val] = index
            index += 1
        return []