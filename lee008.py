import re


class Solution:
    def myAtoi(self, str: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)


sol = Solution()
result = sol.myAtoi("      -11919730356x")
print(result)
