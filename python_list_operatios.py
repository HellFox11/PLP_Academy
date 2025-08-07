# Create an empty list called my_list
my_list = []

# Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)

# Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Sort in ascending order
my_list.sort()
print("After sorting:", my_list)

# print index of 30
print("Index of 30:", my_list.index(30))