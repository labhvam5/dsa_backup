# Multiple recursion calls - This will give a biderctional recursion tree
# Find  nth fibonacci number

def fib(n):
    if n<=1:
        return n
    last = fib(n-1)
    s_last = fib(n-2)
    return last+s_last

print(fib(4))
