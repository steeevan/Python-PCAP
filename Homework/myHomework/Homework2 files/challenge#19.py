# Define a list of phrases.
phrases = [['a','b','c'],['d','e','f'],['g','h','i']]

# Create a shallow copy of the original list using slice notation and the list() function.
shallow_phrases = phrases[0:-1] + [['j','k','l']]
print(shallow_phrases)

# Make a change to the original list and observe the effect on the shallow copies.
phrases[1][0] = "XYZ"
print(shallow_phrases)

# Create a deep copy of the original list using the copy module and observe the effect of changes to the original list.
phrases = [['a','b','c'],['d','e','f'],['g','h','i']]
import copy
deep_phrases = copy.deepcopy(phrases)
print(deep_phrases)
phrases[1][0] = "XYZ"
print(deep_phrases)