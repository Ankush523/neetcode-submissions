class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord('a')] += 1
            fingerprint = tuple(count)
            if fingerprint in dictionary:
                dictionary[fingerprint].append(i)
            else:
                dictionary[fingerprint] = [i]

        group_anagrams = []
        for value in dictionary.values():
            group_anagrams.append(value)

        return group_anagrams
