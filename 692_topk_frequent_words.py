class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        map={}
        words.sort()
        for word in words:
            if word in map:
                map[word]+=1
            else:
                map[word]=1
        ar= [ (map[k],k) for k in map]
        
        ar.sort(key= lambda x: x[0], reverse= True)
        
     
        x=[]
        for a in ar:
            x.append(a[1])
            
        return x[:k]
        
            
            
