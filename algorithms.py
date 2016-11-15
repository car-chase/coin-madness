import random
import math
from _ast import Num

def createCoins(size, weight, fakeWeight):
    coins = []
    rand = math.floor(size * random.random())
    for i in range(0,size):
        if(i == rand):
            coins.append(fakeWeight)
            print("appended 1: ", i)
        else:
            coins.append(weight)
    return coins

def counterfeit(coins):
    # Create the sub arrays
    n = len(coins)
    s1 = coins[0: math.floor(n/3)]
    s2 = coins[math.floor(n/3): 2 * math.floor(n/3)]
    s3 = coins[2 * math.floor(n/3): 3 * math.floor(n/3)]

    if(len(coins) % 3 == 1):
        r = coins[n - 1: n]
    
    if(len(coins) % 3 == 2):
        r = coins[n - 2: n]

    w1 = sum(i for i in s1)
    w2 = sum(i for i in s2)
    w3 = sum(i for i in s3)

    if (w1 > w2 and w1 > w3) or (w2 > w1 and w2 > w3) or (w3 > w1 and w3 > w2): 
        print("Coin is heavier")
    elif (w1 < w2 and w1 < w3) or (w2 < w1 and w2 < w3) or (w3 < w1 and w3 < w2):
        print("Coin is lighter")
    else:
        s4 = s1[0: len(r)]
        w4 = sum(i for i in s4)
        wr = sum(i for i in r)
        if(w4 < wr):
            print("Coin is heavier")
        else:
            print("Coin is lighter")

def findStack(coins):
    heaviest = 0
    count = 1
    while count < len(coins):
        if(coins[count] > coins[heaviest]):
            break
        count += 1
    print("Fake stack is at index:", count)

weight = 10
updown = random.random()
if(updown > .5):
    fakeWeight = weight + 1
else:
    fakeWeight = weight - 1

print("Real:", weight, "Fake:", fakeWeight)
counterfeit(createCoins(1000000, weight, fakeWeight))
findStack(createCoins(1000000, weight, weight + 1))