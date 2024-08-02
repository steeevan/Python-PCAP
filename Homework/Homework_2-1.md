# Class Activity: Advanced Lists

## Objectives
By the end of this class activity, students will be able to:
- Understand and apply advanced list operations, including indexing, slicing, and comprehensions.
- Differentiate between shallow and deep copies of lists.
- Iterate over lists using various methods.
- Utilize common list methods and functions.

## Materials Needed
- Computer with Python installed (or access to an online Python compiler)
- Projector and screen (for teacher demonstrations)
- Printed or digital handouts (optional)

---

## Definitions

### 1. Indexing
Indexing is the process of accessing individual elements of a list using their position within the list. Python lists are zero-indexed, meaning the first element is accessed with index 0.

### 2. Negative Indexing
Negative indexing allows access to elements from the end of the list. The last element is accessed with index -1, the second-to-last with index -2, and so on.

### 3. Slicing
Slicing is a technique used to extract a portion of a list by specifying a start and end index. The syntax for slicing is `list[start:end]`.

### 4. Shallow Copy
A shallow copy creates a new list object but does not create copies of the objects within the list. Instead, it copies references to the objects.

### 5. Deep Copy
A deep copy creates a new list object and also recursively copies all objects within the original list, creating fully independent copies.

### 6. List Comprehension
List comprehension is a concise way to create lists using a single line of code. It consists of an expression followed by a `for` clause, and can include `if` clauses.

### 7. Common List Methods
Common list methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `index()`, `count()`, `sort()`, `reverse()`, and `copy()`.

### 8. Common List Functions
Common list functions include `len()`, `sorted()`, `max()`, and `min()`.

---

## Problems

### Problem 1: Index and Negative Indexing
- Create a list containing the first ten square numbers.
- Access and print the first, fourth, last, and fourth-to-last elements using indexing.

### Problem 2: Advanced List Slicing
- Extract and print elements from a list that have even indexes.
- Extract and print elements in reverse order.
- Extract and print a subset of elements with a stride size of 2 within that subset.
- Extract and print elements with even indexes starting from the 5th element.

### Problem 3: Advanced List Slice Assignment
- Define a list of numbers.
- Substitute a subset of the list with new elements.
- Replace every 3rd element with a new value.
- Replace and resize a subset of the list.
- Delete every other element starting from the second element.

### Problem 4: Shallow and Deep List Copies
- Define a list of phrases.
- Create a shallow copy of the original list using slice notation and the `list()` function.
- Make a change to the original list and observe the effect on the shallow copies.
- Create a deep copy of the original list using the `copy` module and observe the effect of changes to the original list.

### Problem 5: Iterating Lists
- Create a list and iterate over it using a `while` loop.
- Iterate over the list using a `for` loop with the `range` function.
- Iterate over the list using a `for` loop with the `in` operator.
- Iterate over the list using a `for` loop with the `in` operator and the `enumerate` function.

### Problem 6: List Membership
- Test whether an element exists in a list using the `in` operator.
- Test whether an element does not exist in a list using the `not in` operator.

### Problem 7: List Comprehension
- Create a list of the squares of the first 10 positive integers using list comprehension.
- Create a list formed of characters from a string.
- Create a list of all the prime numbers between 1 and 100 using a helper function to check for primes.
- Create a list of all the even numbers between 1 and 100, replacing odd numbers with 0.

### Problem 8: Common List Methods
- Use common list methods like `append()`, `extend()`, `insert()`, `remove()`, `pop()`, and `clear()` to modify a list.
- Use methods like `index()`, `count()`, `sort()`, `reverse()`, and `copy()` on a list.

### Problem 9: Common List Functions
- Use common list functions like `len()`, `sorted()`, `max()`, and `min()` on a list of numbers and a list of letters.

### Problem 10: Multi-Dimensional Arrays
- Create a two-dimensional array and access its elements using nested loops.
- Create a two-dimensional array with list comprehension.
- Update, insert, append, and delete elements in a two-dimensional array.
- Create and manipulate a three-dimensional array.

---

## Submission Guidelines

- Complete each problem in a separate file or notebook.
- Ensure your code is well-commented to explain your logic.
- Submit your work via email or your class's online portal by the end of the class.

---

## Additional Resources

- Refer to your class notes and textbook for additional help.
- Use online resources like [Python Documentation](https://docs.python.org/3/) for further reference.

---

Good luck, and if you have any questions, feel free to ask during the class!