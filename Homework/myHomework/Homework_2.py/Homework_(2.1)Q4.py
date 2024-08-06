# Define a list of phrases.
# Create a shallow copy of the original list using slice notation and the list() function.
# Make a change to the original list and observe the effect on the shallow copies.
# Create a deep copy of the original list using the copy module and observe the effect of changes to the original list.
import copy

my_phrases = [['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l']]
shallow = my_phrases[:3] + [['m','n','o']]
print(shallow)
deep = copy.deepcopy(my_phrases)
print(deep)