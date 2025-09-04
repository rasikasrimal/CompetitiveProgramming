class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        results = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            results.append(word1[i])
            results.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            results.append(word1[i])
            i += 1
        while j < len(word2):
            results.append(word2[j])
            j += 1
        print(results)
        return ''.join(results)