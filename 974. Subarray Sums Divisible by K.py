class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_count = [0] * k
        remainder_count[0] = 1
        
        prefix_sum = 0
        ans = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            ans += remainder_count[remainder]
            
            remainder_count[remainder] += 1
            
        return ans
