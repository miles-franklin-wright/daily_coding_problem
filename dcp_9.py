# Good morning! Here's your coding interview problem for today. [Hard]

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


test = [2, 4, -6, 2, 5]
odds = test[1::2]
evens = test[::2]

print(odds, evens)

sums = []

def add(list, sums):
    posisum = 0
    antisum = 0
    for i in list:
        if i < 0:
            antisum += i
        else:
            posisum += i
    if antisum == 0:
        sums.append(posisum)
    else:
        sums.append(posisum + antisum)
    
add(odds, sums)
add(evens, sums)

def largest(sums):
    if sums[0] > sums[1]:
        print(sums[0])
    else:
        print(sums[1])

largest(sums)