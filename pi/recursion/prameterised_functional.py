# write fcationrial of n number in a parameterised way 

def fact(n, sum):
    if n == 1:
        print(sum)
        return
    sum = sum * n
    fact(n-1, sum)

fact(5, 1)


# functional recursion for sum of n numbers

def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)

print(sum(4))

# functional recursion for factorial of n numbers

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(4))


