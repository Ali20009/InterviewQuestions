
'''class Solution:
    def countPrimes(self, n: int) -> int:
        not_prime = n // 2 -1
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 0
        
        for i  in range(3, n ,2):
            for j in range(3 ,i ,2):
                if j > (i / 2):
                    break 
                if i % j == 0:
                    not_prime += 1
                    break
        return n- 1- (not_prime)
            
a = Solution()
'''
class Solution:
    def countPrimes(self , n : int) -> int:
        z = {0:0, 1:0, 2:0, 3:1, 4:2, 10:4}
        if n in z: return z[n]
        primes = [1] *n

        primes[0] = primes[1] = 0
        for i in range(1 ,int(n**0.5) +1):
            if primes[i] == 1:
                for j in range(i ** 2 , n ,i):
                    primes[j] = 0

        return sum(primes) 


s = Solution()
print(s.count_primes(20))
            

