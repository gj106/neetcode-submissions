class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = [0] * 26 #only uppercases
        i = 0
        res=0
        maxFreq = 0
        for j,c in enumerate(s):
            seen[ord(c)-ord('A')]+=1            
            maxFreq = max(maxFreq, seen[ord(c)-ord('A')])

            while j - i + 1 - maxFreq > k: # current window is greater than k
                # move i and also decrement the freq of s[i]
                seen[ord(s[i])-ord('A')]-=1
                i+=1
            res = max(res, j-i+1)

        return res