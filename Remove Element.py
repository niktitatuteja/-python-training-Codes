class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_index = 0
        for current_num in nums:
            if current_num != val:
                nums[valid_index] = current_num
                valid_index += 1
        return valid_index