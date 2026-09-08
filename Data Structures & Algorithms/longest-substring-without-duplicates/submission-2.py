class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i, j, res = 0, 0, 0
        from collections import defaultdict
        freq = defaultdict(int)

        # Correct way using int


        while j < len(s):
            while  i < len(s) and s[j] in freq and freq[s[j]] >= i:
                i = freq[s[j]] + 1
            freq[s[j]]=j
            j+=1
            res = max(res, j-i)
        return res
        