#  Beginner Level List Operations 

print("----- LIST BASIC OPERATIONS -----")

# 1. Create a list and print it
fruits = ["apple", "banana", "mango"]
print("Fruits List:", fruits)


# 2. Add an item to the list
fruits.append("orange")
print("After Adding Item:", fruits)


# 3. Remove an item from the list
fruits.remove("banana")
print("After Removing Item:", fruits)


# 4. Print all elements using loop
print("Looping through list:")
for fruit in fruits:
    print(fruit)


# 5. Find length of list
print("Total Number of Fruits:", len(fruits))

