#Generate and print a multiplication table for numbers 1 to 'number'.
#Creates a nested list where each sublist contains products i * j for j from 1 to i. 
# Prints each operation, sublist, and the final table.
def multiplication_table(number):
    bigTable = []
    for i in range(1, number + 1):
        smalltable = []
        for j in range(1, i + 1):
            result = i * j
            smalltable.append(result)
            print(f"{i} x {j} = {result}")
        print(smalltable)
        bigTable.append(smalltable)
    print(bigTable)