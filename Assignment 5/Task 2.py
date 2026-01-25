# create list from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)

# Extract first five elements
first_five = numbers[:5] # [:] copy list
print("Extracted first five elements:", first_five)

# Reverse the extracted elements
reversed_list = first_five[::2]  #list[start : end : step] mean -1 entire list, backwards
print("Reversed extracted elements:", reversed_list)