import random
import math
from _ast import Num
from time import sleep

'''to do add a bool parameter'''
def createCoins(size, weight, fakeWeight, has_fake):
    coins = []
    rand = math.floor(size * random.random())
    for i in range(0,size):
        if(i == rand and has_fake):
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
    if first == last:
        return list[first]
    
    sum = 0
    for i in range(first, last + 1):
        sum += list[i]
    
    return sum

def binary_search(list, first, last, fake):
    
    #there is no fake coin
    if fake == 0:
        return -2
    
    #check if the range is small enough to compare and return
    if last - first == 1:
        if list[first] < list[last]:
            return first
        else:
            return last
    elif(last - first == 0):
        return last
    elif(last - first < 0):
        return -1
    
    num1 = 0
    num2 = -1
    
    has_num2 = False
    
    #check if the range is of an odd value    
    if (last - first) % 2 == 0:
        has_num2 = True
        num2 = first
        #print("Num2: ", num2)
        first += 1
    
    #find middle values of the index range
    middle1 = int(last - ((last - first) / 2))
    middle2 = int(last - ((last - first - 1) / 2))
    
    #sum the list values including and between the two index ranges
    sum1 = sumList(list, first, middle1)
    sum2 = sumList(list, middle2, last)
    
    #print("First: ", first, "\tMiddle1: ", middle1,
    #       "\nMiddle2: ", middle2, "\tLast: ", last,
    #        "\nSum1: ", sum1, "\tSum2: ", sum2, "\tRemainder: ", list[num2])
    
    #perform this function recursively based on if the coin is heavier or lighter
    #as determined by counterfeit function
    if fake == -1:
        if sum1 > sum2:
            num1 = binary_search(list, middle2, last, fake)
        elif sum1 == sum2:
            num1 = first
        else:
            num1 = binary_search(list, first, middle1, fake)
        if has_num2:
            if list[num1] > list[num2]:
                return num2
    else:
        if sum1 < sum2:
            num1 = binary_search(list, middle2, last, fake)
        elif sum1 == sum2:
            num1 = first
        else:
            num1 = binary_search(list, first, middle1, fake)
        if has_num2:
            if list[num1] < list[num2]:
                return num2
    
    return num1

def b_tree_search(list, first, last):
    
    #check if the range is small enough to compare and return
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
    
    num1 = 0
    num2 = -1
    num3 = -1
    
    has_one = False
    has_two = False
    
    #check if the range is a multiple of 3
    if(last - first) % 3 == 1:
        has_two = True
        num2 = first
        first += 1
        num3 = first
        first += 1
        #print("Num2: ", num2, "\tNum3: ", num3)
    
    elif(last - first) % 3 == 0:
        has_one = True
        num2 = first
        first += 1
        #print("Num2: ", num2)
    
    #find middle values of the index range
    middle1 = int(last - (last - first) / 3 * 2)
    middle2 = int(last - (last - first - 1) / 3 * 2)
    middle3 = int(last - (last - first) / 3)
    middle4 = int(last - (last - first - 2) / 3)
    #print("First: ", first, "\tmiddle1: ", middle1, "\nmiddle2: ", middle2, "\tmiddle3: ", middle3, "\nmiddle4: ", middle4, "\tLast: ", last)
    
    #sum the list values including and between the two index ranges
    sum1 = sumList(list, first, middle1)
    sum2 = sumList(list, middle2, middle3)
    sum3 = sumList(list, middle4, last)
    
    #print("Sum1: ", sum1, "\tSum2: ", sum2, "\tSum3: ", sum3)
    
    #determine which sum value is smaller (if one is) and call
    #b_tree_search on that range
    if sum1 < sum2:
        if sum1 < sum3:
            num1 = b_tree_search(list, first, middle1)
        else:
            num1 = b_tree_search(list, middle4, last)
    elif sum2 < sum3:
        num1 = b_tree_search(list, middle2, middle3)
    else:
        num1 = b_tree_search(list, middle4, last)
    
    #determine if there is a remainder for this call
    #which num is smaller and set it to num1
    if has_two:
        if list[num1] < list[num2]:
            if list[num1] > list[num3]:
                num1 = num3
        elif list[num2] < list[num3]:
            num1 = num2
        else:
            num1 = num3
    elif has_one:
        if list[num1] > list[num2]:
            num1 = num2
    
    #return num1 to previous call
    return num1
    
def random_func():
    updown = random.random()
    print("Random: ", updown)
    if(updown > .5):
        sleep(random.random())
        return True
    else:
        sleep(random.random())
        return False

if __name__ == '__main__':
    size = 1000000
    weight = 10
    fakeWeight = weight
    if(random_func()):
        fakeWeight = weight + 1
    else:
        fakeWeight = weight - 1

    print("Real:", weight, "Fake:", fakeWeight)
    counterfeit(createCoins(size, weight, fakeWeight, True))
    findStack(createCoins(size, weight, weight + 1, True))
    print("\n")
    print("Binary Search: ", binary_search(createCoins(size, weight, weight - 1, True), 0, size - 1, -1))
    print("\n")
    print("Binary Search: ", binary_search(createCoins(size, weight, weight + 1, True), 0, size - 1, 1))
    print("\n")
        
    # Create an array that randomly has a fake coin at a random position
    if(random_func()):
        fakeWeight = weight - 1
    else:
        fakeWeight = weight + 1

    coins = createCoins(size, weight, fakeWeight, random_func())
    print("Binary Search: ", binary_search(coins, 0, size - 1, counterfeit(coins)))
    print("\n\n")
    print("B_tree_search: ", b_tree_search(createCoins(size, weight, weight -1, True), 0, size - 1))