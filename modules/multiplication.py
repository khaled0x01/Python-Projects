#Print the multiplication table for a given number.
#Prints the products of 'n' multiplied by numbers 1 to 'n'
def multiplication(n):
    for i in range(1, n+1):
        print(f"{n} * {i} = {n*i}")