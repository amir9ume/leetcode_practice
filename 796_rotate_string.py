class Solution(object):
    
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        
        ctr=len(s)-1
        flag=True
        while(flag):
            if goal[:ctr] in s:
                temp=goal[:ctr]
                goal=goal.replace(temp,'')
                s=s.replace(temp,'')
              
                if s==goal:
                    return True
                else:
                    return False
                flag= False
            else:
                ctr-=1
        
