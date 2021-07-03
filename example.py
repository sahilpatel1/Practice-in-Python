#let's convert binary to decimal

import math
x = 12 #stores 12 as an integer

def decimal_to_binary():
    global x
    quotient = x
    binary_list = [] #list that stores the series of 1's and 0's
    while(quotient >= 0):
        binary_list.append(quotient % 2)
        quotient = quotient // 2

    print(binary_list)



print(math.pow(2,4)) #should return 16 because 2 * 2 * 2 * 2 = 16
decimal_to_binary()