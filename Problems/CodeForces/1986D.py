def max_profit(n ,a ,b):
    i = 0
    profit = 0
    while b - i > a and i <= n:
        profit += b - i
        i += 1
    return profit + (n - i)*a


#print(max_profit(10, 10,5))
#the number of buns,
#  the usual price of a bun, 
# and the price of the first bun to be sold at a modified price.