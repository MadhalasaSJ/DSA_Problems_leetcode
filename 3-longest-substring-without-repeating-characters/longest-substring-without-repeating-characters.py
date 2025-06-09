class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = {}
        start = 0
        max_length = 0
        
        # Traverse the string and update the count of characters
        for end in range(len(s)):
            # If the character is already in the substring, update start
            if s[end] in char_count and char_count[s[end]] >= start:
                start = char_count[s[end]] + 1  # Move start to the right of the duplicate
            
            # Update the last seen index of the character
            char_count[s[end]] = end
            
            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)
        
        return max_length           

        