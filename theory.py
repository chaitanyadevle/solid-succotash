import array as arr

# 'd' is type_code for double.
# 'f' for float.
# 'l' for long.
# 'i' for int.

a = arr.array("d", [1.1, 2.2, 3.3])
print(a)

a = arr.array("i", [2, 3, 6, 4, 2, 5, 8])

# Accessing Values:
print(a[0])
print(a[1])
print(a[-1])

# Slicing
print(a[:], "Entire array")
print(a[3:], "4th to end")
print(a[:6], "Start to 6th")

# Changing Elements
a[0] = 0
a[3:5] = arr.array("i", [9, 2])
print(a)

# append() / extend()
a.append(11)
print(a)
a.extend([19, 18, 17])
print(a)

# + operator to concatenate arrays.
odd = arr.array("i", [1, 3, 5])
even = arr.array("i", [2, 4, 6])
print(odd + even)

# Deleting array elements or entire array
del a[4]
print(a)

# del a
# print(a)

# pop() / remove()

# pop takes index as an argument.
a.pop(2)
print(a)

# remove takes argument that is to be removed
# Deletes only first occurence.
a.remove(8)
print(a)
