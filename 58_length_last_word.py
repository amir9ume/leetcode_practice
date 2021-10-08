class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words= s.split(' ')
        
        for j in range(len(words)-1,-1,-1):
            word=words[j]
            if len(word)>0:
                return len(word)
        
