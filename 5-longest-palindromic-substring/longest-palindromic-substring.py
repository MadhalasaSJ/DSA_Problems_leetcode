class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        start, max_len = 0, 1 

        def center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    start = left
                    max_len = curr_len

                left -= 1
                right += 1

        for i in range(n):
            center(i,i)

            center(i, i+1)
        return s[start:start+max_len]       

        