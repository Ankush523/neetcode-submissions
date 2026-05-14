from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        s1_len = len(s1)
        l=0
        r=0
        window_freq = Counter()

        while(r<len(s2)):
            window_freq[s2[r]]+=1
            if r-l+1 == s1_len :
                if window_freq == freq_s1:
                    return True
                window_freq[s2[l]]-=1
                if window_freq[s2[l]] == 0:
                    del window_freq[s2[l]]
                l+=1
            r+=1
        return False