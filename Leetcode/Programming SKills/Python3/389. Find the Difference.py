class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = [char1 for char1, char2 in zip(sorted(s), sorted(t)) if char1 != char2]
        print(diff)