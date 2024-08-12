from collections import Counter
'''class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic=Counter(secret)-Counter(guess)
        cnt=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                cnt+=1
        cnt2=len(secret)-sum(dic.values())-cnt
        return str(cnt)+"A"+str(cnt2)+"B"
'''
class Solution:
    def getHint(self, secret, guess):
        secret_dict = {}
        guess_dict = {}
        #Bulls
        A , B = 0,0
        for x,y in zip(secret , guess):
            if x == y:
                A += 1
            #Cows
            secret_dict[x] = secret_dict.get(x,0) +1
            guess_dict[y] = guess_dict.get(y,0) +1
        for i in secret_dict:
            if i in guess_dict:
                B += min(secret_dict[i] , guess_dict[i]) - A

        return f'{A}A{B}B' ,secret_dict , guess_dict
    
a = Solution()
print(a.getHint("1123" ,"0111"))
#Input: secret = "1123", guess = "0111"
#Output: "1A1B"