class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, stringMap = 0, 0, {}
        for i in range(len(s)):
            position = stringMap.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            stringMap[s[i]] = i
        longest = max(len(s) - start, longest)
        return longest