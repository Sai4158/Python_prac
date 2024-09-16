list  =  [43,53,4]

# appends add in the last 
list.append(5)
print(list)
# [43, 53, 4, 5]


# will sort the list
list.sort()
print(list)
# [4, 5, 43, 53]


# will sort in reverse
list.sort(reverse=True)
print(list)
# [53, 43, 5, 4]

# reverse method
list.reverse()
print(list)
# [4, 5, 43, 53]


# insert method -  adds in the array 
# at index 1 insert 5
list.insert(1,5)
print(list)
# [4, 5, 5, 43, 53]