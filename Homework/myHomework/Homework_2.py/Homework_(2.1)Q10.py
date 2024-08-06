# Create a two-dimensional array and access its elements using nested loops.
# Create a two-dimensional array with list comprehension.
# Update, insert, append, and delete elements in a two-dimensional array.
# Create and manipulate a three-dimensional array.

# What does 'end = ""' do?

confusion = [[1,2,3],[4,5,6],[7,8,9]]
for erm in confusion:
    for no in erm:
        print(no, end=' ')
    print()

arraryayrayry = [[0 for i in range(3)] for j in range(3)]
for a in arraryayrayry:
    for b in a:
        print(b, end=" ")
    print()

biggie = [[1,2,3],[4,5,6],[7,8,9]]

biggie[1][1] = 100
biggie.insert(2,[6,6,6])
biggie.append([10,9,21])
del biggie[2]

for big in biggie:
    for p in big:
        print(p, end= ' ')
    print()

i_hate_3_dimensional_arrays = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]]

i_hate_3_dimensional_arrays[0][0][1] = 100
print(i_hate_3_dimensional_arrays)