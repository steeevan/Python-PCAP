import copy

# Define a list of phrases
phrases = ["xx", "ww", "yy", "zz"]
# Create a shallow copy of the original list using slice notation and the list() function
shallow_copy_slice = phrases[:]
shallow_copy_list = list(phrases)

# Make a change to the original list
phrases[1] = "Deep learning"

print("Original list:", phrases)
print("Shallow copy (slice):", shallow_copy_slice)
print("Shallow copy (list):", shallow_copy_list)

# Create a deep copy of the original list using the copy module
deep_copy = copy.deepcopy(phrases)

# Make another change to the original list
phrases[2] = "xy"

print("Original list:", phrases)
print("Deep copy:", deep_copy)