class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size < 3:
            return 0
        
        leftMax = [0] * size
        rightMax = [0] * size
        

        leftMax[0] = height[0]
        for i in range(1, size):
            leftMax[i] = max(leftMax[i-1], height[i])
            
        rightMax[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
            
        ans = 0
        for i in range(size):

            water_level = min(leftMax[i], rightMax[i])
            if water_level > height[i]:
                ans += water_level - height[i]
                
        return ans
