class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):  
            if n % i == 0: 
                subString = s[:i]  
                repeated = subString * (n // i)  
                if repeated == s: 
                    return True
        return False
