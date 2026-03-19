class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p
        
        if target_rem == 0:
            return 0
        

        prefix_map = {0: -1}
        current_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            
            needed_rem = (current_sum - target_rem + p) % p
            
            if needed_rem in prefix_map:
                min_len = min(min_len, i - prefix_map[needed_rem])
            
            prefix_map[current_sum] = i
            
        return min_len if min_len < len(nums) else -1
