# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


# does this update?

x = [10, 15, 3, 7]
y = []
z = 0
k = 17

def trial(x, y):
    f = []
    for n in x:
        a = n
        for n in x:
            z = a + n
            if z == (k):
                f.append(a)
                f.append(n)
    print(f)
    
    

trial(x, y)

