import random
import math
from _ast import Num
from time import sleep

'''to do add a bool parameter'''


def create_coins(size, weight, fakeWeight, has_fake):
    """
    Function to create a list of coins; may or may not contain a counterfeit coin.
    :param size: The amount of coins to add to our coin list
    :param weight: Integer representing the weight of a real coin
    :param fakeWeight: Integer representing the weight of a fake coin
    :param has_fake: Boolean to determine whether or not to include a fake coin in the list
    :return: Returns a list 'coins' filled with various different weights
    """
    # Create an empty list 'coins'
    coins = []
    # Determine a random place in the list to put a fake coin
    rand = math.floor(size * random.random())
    # Assign each index of the list a weight
    for i in range(0, size):
        if i == rand and has_fake:
            coins.append(fakeWeight)
            print("Appended Fake Coin At Index: ", i)
        else:
            coins.append(weight)
    # Return the list of coins
    print("create_coins() ran successfully, coin list created.")
    return coins


def counterfeit(coins):
    """
    Function to determine whether or not a list of coins contains a counterfeit coin, will NOT determine exactly
    where that coin exists if there is one.
    :param coins: A list of coins. Each index contains a weight. There will only ever be AT MOST two different weights
    :return: Will return a number based on the result
                -1 == There is a fake coin and it is lighter than the rest
                0 == There is no fake coin in the list
                1 == There is a fake coin and it is heavier than the rest
    """

    # Create the sub arrays
    n = len(coins)
    s1 = coins[0: math.floor(n / 3)]
    s2 = coins[math.floor(n / 3): 2 * math.floor(n / 3)]
    s3 = coins[2 * math.floor(n / 3): 3 * math.floor(n / 3)]
    # If there are leftover coins after dividing the list by 3, we must create a "leftover" list
    if len(coins) % 3 == 1:
        r = coins[n - 1: n]
    elif len(coins) % 3 == 2:
        r = coins[n - 2: n]
    else:
        r = []
    # Find the sum of the weights for each of the sub arrays
    w1 = sum(i for i in s1)
    w2 = sum(i for i in s2)
    w3 = sum(i for i in s3)
    # If one group weighs more than the rest, we know that there is a heavier fake coin
    if (w1 > w2 and w1 > w3) or (w2 > w1 and w2 > w3) or (w3 > w1 and w3 > w2):
        print("counterfeit() found that the coin is heavier")
        return 1
    # If one group weighs less than the rest, we know that there is a lighter fake coin
    elif (w1 < w2 and w1 < w3) or (w2 < w1 and w2 < w3) or (w3 < w1 and w3 < w2):
        print("counterfeit() found that the coin is lighter")
        return -1
    # Otherwise, we have to check the leftover coins (if they even exist)
    else:
        s4 = s1[0: len(r)]
        w4 = sum(i for i in s4)
        wr = sum(i for i in r)
        if w4 < wr:
            print("counterfeit() found that the coin is heavier")
            return 1
        elif w4 > wr:
            print("counterfeit() found that the coin is lighter")
            return -1
        else:
            print("counterfeit() found that there is no fake coin")
            return 0


def find_stack(coins):
    """
    Find which index contains the fake stack of coins; since we only need one coin from each stack (every coin in each
    stack weighs the same), each index represents a stack of coins.length coins.
    :param coins: A list of coins. Each index contains a weight. There will only ever be AT MOST two different weights
    :return: Just print out where the fake stack of coins is located at
    """
    heaviest = 0
    count = 1
    while count < len(coins):
        if coins[count] > coins[heaviest]:
            break
        count += 1
    print("Fake stack is at index:", count)


def sum_list(input_list, first, last):
    """
    :param input_list: A list of coins
    :param first: The first index to be included in the sum
    :param last: The last index to be included in the sum
    :return: The sum of the weights from the inputted list
    """
    # If the first and last indexes are the same, simply return the weight at that index
    if first == last:
        return input_list[first]

    list_sum = 0
    for i in range(first, last + 1):
        list_sum += input_list[i]

    return list_sum


def binary_search(input_list, first, last, fake):
    """
    Implements a binary search to be done on input_list, in between the indexes 'first' and 'last'
    :param input_list: The list on which to do the binary search
    :param first: First index of the input_list to include in the search
    :param last: Last index of the input_list to include in the search
    :param fake:
    :return: Return an integer based on the result of the search/fake input
    """
    # If fake is 0, then there is no fake coin, return -2
    if fake == 0:
        return -2

    # Check if the range is small enough to compare and return
    if last - first == 1:
        if input_list[first] < input_list[last]:
            return first
        else:
            return last
    elif last - first == 0:
        return last
    elif last - first < 0:
        return -1

    num1 = 0
    num2 = -1

    has_num2 = False

    # check if the range is of an odd value
    if (last - first) % 2 == 0:
        has_num2 = True
        num2 = first
        # print("Num2: ", num2)
        first += 1

    # find middle values of the index range
    middle1 = int(last - ((last - first) / 2))
    middle2 = int(last - ((last - first - 1) / 2))

    # sum the list values including and between the two index ranges
    sum1 = sum_list(input_list, first, middle1)
    sum2 = sum_list(input_list, middle2, last)

    # print("First: ", first, "\tMiddle1: ", middle1,
    #       "\nMiddle2: ", middle2, "\tLast: ", last,
    #        "\nSum1: ", sum1, "\tSum2: ", sum2, "\tRemainder: ", list[num2])

    # perform this function recursively based on if the coin is heavier or lighter
    # as determined by counterfeit function
    if fake == -1:
        if sum1 > sum2:
            num1 = binary_search(input_list, middle2, last, fake)
        elif sum1 == sum2:
            num1 = first
        else:
            num1 = binary_search(input_list, first, middle1, fake)
        if has_num2:
            if input_list[num1] > input_list[num2]:
                return num2
    else:
        if sum1 < sum2:
            num1 = binary_search(input_list, middle2, last, fake)
        elif sum1 == sum2:
            num1 = first
        else:
            num1 = binary_search(input_list, first, middle1, fake)
        if has_num2:
            if input_list[num1] < input_list[num2]:
                return num2

    return num1


def b_tree_search(input_list, first, last, fake):
    """
    :param input_list: The list of coins to do the search on
    :param first: The first index to include in the b-tree search
    :param last: The last index to include in the b-tree search
    :return:
    """
    if fake == 0:
        return -2

    list_range = last - first
    # Check if the range is small enough to compare and return (if there are only 3 values in the list)
    if list_range == 2:
        # If first index is less than 2nd index...
        if input_list[first] < input_list[first + 1]:
            # If fake shows a light coin, and first is less than the last as well as the 2nd, then return first
            if input_list[first] < input_list[last] and fake == -1:
                print("Coin is light!")
                return first
            # If first is equal to last and we're looking for a heavier coin, return the 2nd index
            elif input_list[first] == input_list[last] and fake == 1:
                print("Coin is heavy!")
                return first + 1
            # If first index is less than the 2nd index but not the 3rd...
        # If first is heavier than 2nd...
        elif input_list[first] > input_list[first + 1]:
            # If first is heavier than last, and fake is searching for a heavy, return first
            if input_list[first] > input_list[last] and fake == 1:
                print("Coin is heavy!")
                return first
            # If the first index equals the last, then the 2nd is light, return 2nd index
            elif input_list[first] == input_list[last] and fake == -1:
                print("Coin is light!")
                return input_list[first + 1]
        # If the first index == 2nd index, we know the fake is in the 3rd index
        else:
            if input_list[first + 1] < input_list[last] and fake == -1:
                print("Coin is light!")
                return last
            else:
                print("Coin is heavy!")
                return last

    elif list_range == 1:
        if input_list[first] < input_list[last]:
            # If fake shows that it is lighter, then return the lighter coin
            if fake == -1:
                return first
            else:
                return last

    elif list_range == 0:
        return last
    elif list_range < 0:
        return -1

    num1 = 0
    num2 = -1
    num3 = -1

    has_one = False
    has_two = False

    # check if the range is a multiple of 3
    if list_range % 3 == 1:
        has_two = True
        num2 = first
        first += 1
        num3 = first
        first += 1
        list_range -= 2
        # print("Num2: ", num2, "\tNum3: ", num3)

    elif list_range % 3 == 0:
        has_one = True
        num2 = first
        first += 1
        list_range -= 1
        # print("Num2: ", num2)

    # find middle values of the index range
    middle1 = int(last - (list_range) / 3 * 2)
    middle2 = int(last - (list_range - 1) / 3 * 2)
    middle3 = int(last - (list_range) / 3)
    middle4 = int(last - (list_range - 2) / 3)
    # print("First: ", first, "\tmiddle1: ", middle1, "\nmiddle2: ", middle2, "\tmiddle3: ", middle3, "\nmiddle4: ",
    #        middle4, "\tLast: ", last)

    # sum the list values including and between the two index ranges
    sum1 = sum_list(input_list, first, middle1)
    sum2 = sum_list(input_list, middle2, middle3)
    sum3 = sum_list(input_list, middle4, last)

    # print("Sum1: ", sum1, "\tSum2: ", sum2, "\tSum3: ", sum3)

    # Determine which sum value is smaller (if one is) and call
    # b_tree_search on that range
    if fake == -1:
        if sum1 < sum2:
            if sum1 < sum3:
                num1 = b_tree_search(input_list, first, middle1, fake)
            else:
                num1 = b_tree_search(input_list, middle4, last, fake)
        elif sum2 < sum3:
            num1 = b_tree_search(input_list, middle2, middle3, fake)
        else:
            num1 = b_tree_search(input_list, middle4, last, fake)
    elif fake == 1:
        if sum1 > sum2:
            if sum1 > sum3:
                num1 = b_tree_search(input_list, first, middle1, fake)
            else:
                num1 = b_tree_search(input_list, middle4, last, fake)
        elif sum2 > sum3:
            num1 = b_tree_search(input_list, middle2, middle3, fake)
        else:
            num1 = b_tree_search(input_list, middle4, last, fake)

    # determine if there is a remainder for this call
    # which num is smaller and set it to num1
    if has_two:
        if fake == -1:
            if input_list[num1] < input_list[num2]:
                if input_list[num1] > input_list[num3]:
                    num1 = num3
            elif input_list[num2] < input_list[num3]:
                num1 = num2
            else:
                num1 = num3
        if fake == 1:
            if input_list[num1] > input_list[num2]:
                if input_list[num1] < input_list[num3]:
                    num1 = num3
            elif input_list[num2] > input_list[num3]:
                num1 = num2
            else:
                num1 = num3
    elif has_one:
        if fake == -1:
            if input_list[num1] > input_list[num2]:
                num1 = num2
        if fake == 1:
            if input_list[num1] < input_list[num2]:
                num1 = num2

    # return num1 to previous call
    return num1


def random_func():
    """
    Function that generates a random number and uses it to determine whether the fake coin will be heavier or lighter
    :return: Boolean value to determine weight of fake coin (heavier or lighter)
                    True == heavier
                    False == lighter
    """
    updown = random.random()
    print("Random: ", updown)
    if updown > .5:
        sleep(random.random())
        return True
    else:
        sleep(random.random())
        return False


def determine_fake():
    """
    Simple function to determine if there should be a fake coin for problem 3; small chance of no fake.
    :return: Boolean to determine whether or not to include a fake coin for problem 3
                    True == include fake
                    False == do not include fake
    """
    fake_num = random.random()
    print("Random for fake coin: ", fake_num)
    if fake_num > .85:
        return False
    return True

if __name__ == '__main__':
    # Create size and weight variables, size == number of coins to put into a list, weight == weight of a genuine coin
    size = 24
    weight = 10
    # Originally initialize fakeWeight as the same weight as a real coin
    fakeWeight = weight
    # Change fakeWeight based on the result of random_func()
    if random_func():
        fakeWeight = weight + 1
    else:
        fakeWeight = weight - 1

    # Print the real weight and fake weight
    print("Real:", weight, "Fake:", fakeWeight)

    # Create list of coins for each problem (since each problem varies slightly)

    coins_prob1a = create_coins(size, weight, fakeWeight, True)
    coins_prob1b = create_coins(size, weight, 11, True)
    # Problem 2 will always have a fake, lighter coin
    coins_prob2 = create_coins(size, weight, 9, True)
    print("\n")

    # Call the O(n) search function find_stack() to find which index contains the stack of fake coins
    # This call is for problem 1 (Brute Force Solution)
    print("Problem 1 Start: ")
    counterfeit(coins_prob1a)
    find_stack(coins_prob1a)
    """
    print("\n")
    print("Binary Search: ", binary_search(create_coins(size, weight, weight - 1, True), 0, size - 1, -1))
    print("\n")
    print("Binary Search: ", binary_search(create_coins(size, weight, weight + 1, True), 0, size - 1, 1))
    print("\n")
    """
    print("End Problem 1\n")
    print("Problem 2 Start: ")
    print("Divide-into-two (binary search) result: ", binary_search(coins_prob2, 0, size - 1, counterfeit(coins_prob2)))
    print("Divide-into-three result: ", b_tree_search(coins_prob2, 0, size - 1, counterfeit(coins_prob2)))
    print("End Problem 2")

    # Start Problem 3 (May not have a fake coin)
    # Create a new list of coins with the same size, same fake weight, but with the possibility of NOT having a fake
    coins_prob3 = create_coins(size, weight, fakeWeight, determine_fake())
    print("Start Problem 3: ")
    print("Fake index (if exists): ", b_tree_search(coins_prob3, 0, size - 1, counterfeit(coins_prob3)))

