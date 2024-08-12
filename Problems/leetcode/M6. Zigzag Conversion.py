'''import numpy as np

class Solution:
    def convert(self, s, numRows) -> str:
        a= numRows*2 -2
        b = len(s) % a - numRows
        if b > 0:
            column = (numRows-1) * (len(s) // a) +  b +1
        if b == 0:
            column = (numRows-1) * (len(s) // a) 
        else:
            column = (numRows-1) * (len(s) // a) +1
        
        matrix = np.empty((numRows,column) ,dtype='object')
        
        c = 0
        r = 0
        while c < len(s):
            for i in range(numRows):
                matrix[i , r]  = s[i]
            

        return matrix , column
    '''
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        r=['']*numRows
        c=0
        g=False
        for i in s:
            r[c]+=i
            if c==0 or c==numRows-1:
                g=not g
            #c+=1 if g else -1
            if g:
                c+=1
            else:
                c-=1
        return   ''.join(r), r
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [''] * numRows

        t = False
        b = 0
        for a in s:
            res[b] += a
            if b == numRows-1 or b == 0:
                t = not t
            if t:
                b += 1
            if not t:
                b -= 1
    
        return ''.join(res)

a = Solution()
print(a.convert('PAYPALISHIRING', 4))
'PALIGYAIHRNPSI'