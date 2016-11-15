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
		return 1
    elif (w1 < w2 and w1 < w3) or (w2 < w1 and w2 < w3) or (w3 < w1 and w3 < w2):
        print("Coin is lighter")
		return -1
    else:
        s4 = s1[0: len(r)]
        w4 = sum(i for i in s4)
        wr = sum(i for i in r)
        if(w4 < wr):
            print("Coin is heavier")
			return 1
        elif(w4 > wr):
            print("Coin is lighter")
			return -1
        else:
            print("No fake coin")
			return 0

def findStack(coins):
    heaviest = 0
    count = 1
    while count < len(coins):
        if(coins[count] > coins[heaviest]):
            break
        count += 1
    print("Fake stack is at index:", count)
    
def sumList(list, first, last):
    if(first == last):
        return list[first]
    
    sum = 0
    for i in range(first, last + 1):
        sum += list[i]
    
    return sum

def binary_search(list, first, last):
        
    if(last - first == 1):
        if(list[first] < list[last]):
            return first
        else:
            return last
    elif(last - first == 0):
         return last
    elif(last - first < 0):
        return -1
    
    last1 = int(last - ((last - first) / 2))
    last2 = int(last - ((last - first - 1) / 2))
    #print("First: ", first, "\tLast1: ", last1, "\nLast2: ", last2, "\tLast: ", last)
    
    num1 = sumList(list, first, last1)
    num2 = sumList(list, last2, last)
    
    #print("Num1: ", num1)
    #print("Num2: ", num2)
    
    
    if(num1 > num2):
        return binary_search(list, last2, last)
    else:
        return binary_search(list, first, last1)
    
def b_three_search(list, first, last):
    
    if(last - first == 2):
        if(list[first] < list[first + 1]):
            if(list[first] < list[last]):
                return first
            else:
                if(list[first + 1] < list[last]):
                    return first + 1
                else:
                    return last
        else:
            if(list[first + 1] < list[last]):
                return first + 1
            else:
                return last
        
    elif(last - first == 1):
        if(list[first] < list[last]):
            return first
        else:
            return last
    elif(last - first == 0):
         return last
    elif(last - first < 0):
        return -1
    middle1 = int(last - (last - first) / 3 * 2)
    middle2 = int(last - (last - first - 2) / 3 * 2)
    middle3 = int(last - (last - first) / 3)
    middle4 = int(last - (last - first - 3) / 3)
    print("First: ", first, "\tmiddle1: ", middle1, "\nmiddle2: ", middle2, "\tmiddle3: ", middle3, "\nmiddle4: ", middle4, "\tLast: ", last)
    
    num1 = sumList(list, first, middle1)
    num2 = sumList(list, middle2, middle3)
    num3 = sumList(list, middle4, last)
    
    print("/nNum1", num1, "Num2", num2, "Num3", num3)
    
def random():
	updown = random.random()
    if(updown > .5):
        return true
    else:
        return false

if __name__ == '__main__':
    size = 1000000
    weight = 10
    if(random()):
        fakeWeight = weight + 1
    else:
        fakeWeight = weight - 1

	print("Real:", weight, "Fake:", fakeWeight)
	counterfeit(createCoins(size, weight, fakeWeight))
	findStack(createCoins(size, weight, weight + 1))
	print("Binary Search: ", binary_search(createCoins(size, weight, weight - 1), 0, size - 1))
	b_three_search(createCoins(size, weight, weight -1), 0, size - 1)
	
	# Create an array that randomly has a fake coin at a random position
	if(random()):
		fakeWeight = weight
	else:
		fakeWeight = weight + 1