#Generate a shifting star pattern
#Creates a list of 'size' spaces, iteratively replaces the first space with '*', and prints the resulting string, producing a pattern where stars shift right.
def mario2(size):
    my_list = [" "] * size
    for i in range(len(my_list)):
        my_list.pop(0)
        my_list.append("*")
        print(''.join(my_list))