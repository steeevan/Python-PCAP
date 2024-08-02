# Define a list of phrases.
phrases = [['a', 'c', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]

# Create a shallow copy of the original list using slice notation and the list() function.
shallow = phrases[:2] + [['sadf', 'fdsa', 'asdf']]
print(shallow)

# Make a change to the original list and observe the effect on the shallow copies.
shallow = phrases[:2] + [['sadf', 'fdsa', 'asdf']]
print(shallow)

# Create a deep copy of the original list using the copy module and observe the effect of changes to the original list.
import copy
my_deep_phrases = copy.deepcopy(phrases)
print(my_deep_phrases)