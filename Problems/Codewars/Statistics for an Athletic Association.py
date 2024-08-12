'''import time
def stat(strg):
    
    if strg == '':
        return strg
    strg = strg.split(', ')
    strg = [component.split('|') for component in strg]
    for i in strg:
        i[0] = int(i[0]) * 3600
        i[1] = int(i[1]) * 60
        i[2] = int(i[2])
    a = []
    for component in strg:
        a.append(sum(component))
    
    #Median
    if len(a) /2 == len(a) //2:
        Median = int((sorted(a)[int(len(a) /2)] + sorted(a)[int(len(a) /2) -1]) /2 )
    else:
        Median = int(sorted(a)[len(a) //2])
    Median = time.strftime('%H|%M|%S' , time.gmtime(Median))
    
    #Range
    range = max(a) - min(a)
    range = time.strftime('%H|%M|%S', time.gmtime(range))

    #Average
    Average = sum(a) /len(a)
    Average = time.strftime('%H|%M|%S')
    
    return f"Range: {range} Average: {Average} Median: {Median}"
    
            
'''
v = ('01|15|59, 1|47|6')
a = [sum(x*y for x ,y in zip([3600 ,60, 1] ,map(int,i.split('|'))))for i in v.split(', ')]
print(a)
from statistics import mean, median
def stat(strg):
    if not strg: return ''

    s = [sum(x * y for x,y in zip([3600, 60, 1], map(int, i.split('|'))))for i in strg.split(', ') ] # Genius
    f = lambda x: f'{int(x//3600):02}|{int(x%3600//60):02}|{int(x%60):02}'
    return  f'Range: {f(max(s) - min(s))} Average: {f(mean(s))} Median: {f(median(s))}'
