class Solution:
    def countDistinct(self, s: str) -> int:
        map={}
        size= len(s)
        
        ct=0
        i=0
        while(i<size):
            c= s[i]
            if c not in map:
                map[c]=True
                ct+=1
            j=i+1
            while(j<size):
                c= c + s[j]
                if c not in map:
                    map[c]=True
                    ct+=1
                j+=1
            
            i+=1
            
        return ct
