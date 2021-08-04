# UNSOLVED. I was able to figure out a lot, but I am now 15 over the hour time limit, meaning I would've failed in an interview. It's healthy to get wrong answers, as long as I eventually get more of them correct. I could likely figure this out (doesn't cover stuff I don't know, at least in simple terms), but it would take a lot more time

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


# OPTION 1 = if I am allowed to create a new array
# implementation plan:
# sort array
# return all values >=0 (sorted) above into a new array
# return length n of array
# check for presence of integers from 1 to length n of array
# if an integer is missing, it will be the default lowest integer

array = [-3, 0, 8, 4, 20, -63, 3, 3, 1, 2]
count = 0
new = []
lowest = None
array.sort()
for n in array:
    if n <=0:
        count += 1
    else:
        new.append(n)
check = []
# check for item in 
previous = 0
current = 0
val = None

if new[0] > 1:
    val = 1
else:
    for m in new:
        current = m
        previous = m - 1
        print(current, previous)


    
    







# OPTION 2 = if I am only allowed to modify the existing array
# implementation plan:
# sort array
# count and move all values <= 0 to end of array
# return length n - length m of <=0
# check for presence of integers from 1 to length n of array
# if an integer is missing, it will be the default lowest integer