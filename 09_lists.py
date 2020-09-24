listA=["Josh", 30, "Jill" , 40]
print(listA)

listA.append("Matt")
print(listA)

print(listA.index("Josh"))
print(listA.index("Jill"))
print(listA.index("Matt"))
#print(listA.index("30"))

listA[3]=45
print(listA)

print(len(listA))

# Removes a specified object from an List
listA.remove("Matt")
print(listA)


# Removes the object at the index specified
listA.pop(0)

# what does this do? Run to find only the numbers in the list display.
listA.pop(1)
print(listA)
# Creates a tuple, a sequence of immutable Python objects that cannot be changed
firstTuple = ('Python',100, 'VBA', False)
print(firstTuple)