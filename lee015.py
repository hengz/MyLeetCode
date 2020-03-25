class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        has = {}
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if has.get(nums[j], None) is not None:
                    res.append(has[nums[j]] + [nums[j]])
                    del has[nums[j]]
                else:
                    has[-(nums[i] + nums[j])] = [nums[i], nums[j]]

        return res


sol = Solution()
result = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(result)
