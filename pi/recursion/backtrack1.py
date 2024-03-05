# Print 1 to n without using + sign
def print_line(i ):
    if i < 1:
        return
    print_line(i-1)
    print(i)

print_line(4)

# Not bracktrack version with a simple recursion tree
def print_line(i, n):
    if i > n:
        return
    print(i)
    print_line(i+1,n)
    
print_line(1,4)
