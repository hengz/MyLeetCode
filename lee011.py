class Solution:
    def maxArea(self, height: [int]) -> int:
        i = 0
        j = 0
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
