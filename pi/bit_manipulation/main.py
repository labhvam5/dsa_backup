# And (&)
# OR (|)

# Xor (^) 
# Even no. of 1's -> 0
# Odd no. of 1's -> 1 

#  2 = 10 , 5 = 101 ^ 000 

# Negation (~)

# Right shift (>>)

# Left shift (<<)


# Single Number leetcode

# Swap using xor 
a = 5
b = 7

print("{} {}".format(a,b))

a = a^b
b = a^b
a = a^b

print("{} {}".format(a,b))

# xor till n number using O(1) complexity

def check(n):
    if n%4 == 0:
        return n
    if n%4 == 1:
        return 1
    if n%4 == 2:
        return n+1
    if n%4 == 3:
        return 0



