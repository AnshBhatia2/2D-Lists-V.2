#creating a 2d list
matrix=[
    [43,64,45],
    [54,76,25],
    [39,95,48]
]
"""
print(matrix)

#finding the number of items in matrix/number of rows
print(len(matrix))

#calculate number of columns
print(len(matrix[0]))

#accessing elements in a list
print(matrix[0][1])
print(matrix[2][1])

#using for loop to print all the items in matrix 
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        print(matrix[row][column],end=" ")
    print()

#take an input for a matrix and print all the element
matrix2 = []
rows = int(input("How many rows do you want?"))
columns = int(input("How many columns do you want?"))
for row in range(rows):
    templist = []
    for column in range(columns):
        item = input("What would you like to add?")
        templist.append(item)

    matrix2.append(templist)

print(matrix2)
"""
#program for addition subtraction of 2d list
matrixA = [
    [1,4],
    [0,9]
]

matrixB = [
    [1,9],
    [8,6]
]

addition = [
    [0,0],
    [0,0]
]

for row in range(len(matrixA)):
    for column in range(len(matrixA[0])):
        addition[row][column]=matrixA[row][column]+matrixB[row][column]

print(addition)

subtraction = [
    [0,0],
    [0,0]
]

for row in range(len(matrixA)):
    for column in range(len(matrixA[0])):
        subtraction[row][column]=matrixA[row][column]-matrixB[row][column]

print(subtraction)

multiplication = [
    [0,0],
    [0,0]
]

for row in range(len(matrixA)):
    for column in range(len(matrixA[0])):
        multiplication[row][column]=matrixA[row][column]*matrixB[row][column]

print(multiplication)