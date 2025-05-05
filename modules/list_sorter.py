#Collect and sort a user-specified number of integers
def sort_user_input(num_elements):
    my_list = []
    for i in range(num_elements):
        n = int(input(f"Enter element {i+1}: "))
        my_list.append(n)
    ascending_order = sorted(my_list)
    descending_order = sorted(my_list, reverse=True)
    print(f"ascending order is: {ascending_order}")
    print(f"descending order is: {descending_order}")