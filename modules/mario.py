#Print a right-aligned triangle of stars
def mario(n):
    for i in range(1, n+1):
        print((n - i) * " " ,end="")
        print("*" * i)