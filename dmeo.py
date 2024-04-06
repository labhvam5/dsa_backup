import sys
sys.stdout = open('/home/labhvam5/Documents/dsa_backup/output.txt', 'w')
sys.stdin = open('/home/labhvam5/Documents/dsa_backup/input.txt', 'r')

x = int(input())
y = int(input())

def maxBottlesDrunk(numBottles: int, numExchange: int) -> int:
    tot = numBottles
    c = 0
    while(c + tot >= numExchange):
        tot = tot - numExchange
        c = c+1
        numExchange = numExchange+1
    return numBottles+c
        
                
    
print(maxBottlesDrunk(x, y))

