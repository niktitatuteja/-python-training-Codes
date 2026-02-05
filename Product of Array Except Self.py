
nums = [1, 2, 3, 4]
n = len(nums)
output = [1] * n
left = 1
for i in range(n):
    output[i] = left
    left *= nums[i]
    right = 1
for i in range(n-1, -1, -1):
    output[i] *= right
    right *= nums[i]
print(output)