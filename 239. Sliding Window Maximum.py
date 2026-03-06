class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = [] 
        res = []
        
        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.pop(0)
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res
