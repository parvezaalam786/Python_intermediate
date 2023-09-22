# Lists: collection datatype that is ordered, mutable, allows duplicate elements
# mutable: we can add elements after the list creation

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist02 = list()
print(mylist02)

mylist03 = [5, True, "apple", "apple", "cherry"]
print(mylist03)

item = mylist03[3]
item2 = mylist03[-3]
print(item, item2)

for i in mylist03:
    print(i)

if "apple" in mylist03:
    print("Yes")
else:
    print("no")

print(len(mylist03))

mylist03.append("lemon")
print(mylist03)

mylist03.insert(2, "banana")
print(mylist03)

lastItem = mylist03.pop()
print(lastItem)
print(mylist03)

mylist03.remove("cherry")
print(mylist03)

mylist03.reverse()
print(mylist03)

numbers = [4, 2, -1, 5, 8, 19]
sortedNumbers = sorted(numbers) # Original list does not change
print("Sorted List: ", sortedNumbers)
print("Original List: ", numbers)
numbers.sort() # Original list gets changed
print("Original List", numbers)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e']
print(my_list.count('p'))

# New list with 5 zeros
mylist04 = [0] * 5
print(mylist04)

mylist05 = [1, 2, 3, 4, 5]

combinedList = mylist04 + mylist05
print(combinedList)

# Slicing
mylist06 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist06[2:6]
print(a)

b = mylist06[2:9:2] # step index
print(b)

b = mylist06[2:9:-2]
print(b)

# Reversing a list
mylist07 = mylist06[::-1]
print(mylist07)

# Copying a list
list_org = ["banana", "mango", "apple", "watermelon"]
list_cpy = list_org
list_cpy.append("lemon") # making a change in copied list will change the original list also
print("list_org: ", list_org)
print("list_cpy: ", list_cpy)


list_cpy = list(list_org)
list_cpy.append("lemons")
print("list_org: ", list_org)
print("list_cpy: ", list_cpy)


# List comprehension
list_a = [1, 2, 3, 4, 5, 6]
list_b = [i * i for i in list_a]
print(list_a, list_b)
