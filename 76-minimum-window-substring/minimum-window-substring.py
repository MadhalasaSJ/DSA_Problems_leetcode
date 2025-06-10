from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = Counter()
        required = len(needs := need.keys())
        formed = 0
        
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right, c in enumerate(s):
            window[c] += 1
            # increment `formed` if we fulfill a character requirement
            if c in need and window[c] == need[c]:
                formed += 1
            
            # Try shrinking while window remains valid
            while left <= right and formed == required:
                # Update result if this window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Attempt to shrink
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        
        # Return the best window found
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
