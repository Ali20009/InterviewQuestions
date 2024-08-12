'''from collections import Counter , defaultdict
senarioes = int(input())
roads = []
coins = []

connections = defaultdict(int)

for i in range(senarioes):
    for j in range(int(input())-1):
        roads += map(int, input().split())
        for k in range(2):
            
            connections[int(roads[j][k])] +=  1

 
print(connections)
print(roads)

for key,value in connections.items():
    coins.append(value)


print(sorted(coins))'''
'''
2
2
2 1
8
7 3
4 6
1 7
5 4
7 4
2 7
8 4'''


a = [1,2,3]
print(list(reversed(a)))
'''print(max(a))


print(type(sorted(a)))'''