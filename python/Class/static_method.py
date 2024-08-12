class Math:
    @staticmethod
    def odd_or_even(x):
        if x % 2 == 0 :
            return 'Even'
        else:
            return 'Odd'
        
print(Math.odd_or_even(7))