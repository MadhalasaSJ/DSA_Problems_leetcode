class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = {}
        start = 0
        max_length = 0
        
        
        for end in range(len(s)):
            
            if s[end] in char_count and char_count[s[end]] >= start:
                start = char_count[s[end]] + 1  
            
            
            char_count[s[end]] = end
            
            
            max_length = max(max_length, end - start + 1)
        
        return max_length           

        