class Solution:
    def reverseWords(self, s: str) -> str:
        
        words= s.split(' ')
        print(words)
        
        rev= words[::-1]
        st=""
        for r in rev:
            if r=="" or r==" ":
                pass
            else:
                st= st+' '+ r
        
        return st.strip()
