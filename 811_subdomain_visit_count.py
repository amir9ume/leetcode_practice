class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        mapDomains={}
        for cpdomain in cpdomains:
            string= cpdomain.split()
            count=int(string[0])
            domainString=string[1]
            domains= self.getAllDomains(domainString)
            for domain in domains:
                if domain not in mapDomains:
                    mapDomains[domain]=count
                else:
                    mapDomains[domain]+=count
        soln=[]
        for domain in mapDomains:
            s= str(mapDomains[domain])+" "+domain
            soln.append(s)
        return soln
    
    def getAllDomains(self, st):
        ar=[]
        subs= st.split('.')
        base=subs[-1]
        ar.append(base)
        size= len(subs)
        for i in range(size-2,-1,-1):
            base= subs[i]+'.'+base
            ar.append(base)
        return ar
