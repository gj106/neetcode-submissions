class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for word in strs:

            freq = [0] * 26

            for c in word:
                freq[ord(c) - ord('a')] += 1
            
            res[tuple(freq)].append(word) # res = {freq : [word1, word2...],  }

        return list(res.values())
        