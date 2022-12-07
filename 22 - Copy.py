# Python3 program to implement
# the above problem

# Function to print the matrix
def print_(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print("\n", end="")


# Function to find the diagonal values
def find(arr, n):
    arr[0][0] = (arr[1][2] + arr[2][1]) // 2
    arr[2][2] = (arr[0][1] + arr[1][0]) // 2
    arr[1][1] = (arr[0][0] + arr[1][1]) // 2
    print("\nMatrix with diagonals:")
    print_(arr, n)


# Driver code
arr = [[0, 54, 48],
       [36, 0, 78],
       [66, 60, 0]]

n = 3
print("Matrix initially:")
print_(arr, n)
find(arr, n)

# This code is contributed by Shrikant13