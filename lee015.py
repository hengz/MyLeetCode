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

    def threeSum2(self, nums: [int]) -> [[int]]:
        # nums做排序
        nums.sort()
        # 两边往中间逼近
        res = []
        for i in range(1, len(nums) - 1):
            head = 0
            tail = len(nums) - 1
            while head != i and tail != i:
                if nums[i] + nums[head] + nums[tail] > 0:
                    tail -= 1
                elif nums[i] + nums[head] + nums[tail] < 0:
                    head += 1
                else:
                    res.append([nums[head], nums[i], nums[tail]])
                    head += 1
                    tail -= 1
        return res


sol = Solution()
result = sol.threeSum2([-1, 0, 1, 2, -1, -4])
print(result)
