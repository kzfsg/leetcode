# maintain a window of valid characters
# when we encounter duplicate, we shrink the window to the left BUT track the max window size we've seen
# hashset -> two pointers, left and right for the boundaries
# use set to track characters in window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # case that string is empty
        if not s:
            return 0

        char_set = set()

        left = 0
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]
            while current_char in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(current_char)

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length

        