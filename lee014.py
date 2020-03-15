class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            # 找到字符串开始不同的下标
            while j < min(len(prefix), len(strs[i])) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[0:j]
        return prefix

    def longestCommonPrefix2(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ''
        return self.longestCommonPrefix2_recursion(strs, 0, len(strs) - 1)

    def longestCommonPrefix2_recursion(self, strs: [str], l: int, r: int) -> str:
        if l == r:
            return strs[l]
        else:
            mid = (l+r)//2
            l_lcp = self.longestCommonPrefix2_recursion(strs, l, mid)
            r_lcp = self.longestCommonPrefix2_recursion(strs, mid + 1, r)
            return self.commonPrefix(l_lcp, r_lcp)

    def commonPrefix(self, l_lcp: str, r_lcp: str) -> str:
        min_len = min(len(l_lcp), len(r_lcp))
        for i in range(0, min_len):
            if l_lcp[i] != r_lcp[i]:
                return l_lcp[0:i]
            i += 1
        return l_lcp[:min_len]


sol = Solution()
res = sol.longestCommonPrefix2(["flower","flow","flight"])
print(res)

