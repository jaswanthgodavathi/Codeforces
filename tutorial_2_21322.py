'''ROLL NUMBER: 21322
   NAME: JASWANTH GODAVARTHI
   PROBLEM STATEMENT: GIVEN A MATRIX OF M*N. FIND THE LARGEST SUB-SQUARE MATRIX CONTAINING ALL ZEROES USING DYNAMIC PROGRAMMING 
   CONTRIBUTION: DID IT ALONE 
   TIME COMPLEXITY: O(M*N) WHERE M DENOTES THE NUMBER OF ROWS AND N DENOTES THE NUMBER OF COLUMNS 
    
   TEST CASE: 1 
   SAMPLE INPUT 1: 
   Enter the number of rows in the matrix: 3 
   Enter the number of columns in the matrix: 3
   Enter row 1 (space-separated 0s and 1s): 0 0 1 
   Enter row 2 (space-separated 0s and 1s): 0 0 1
   Enter row 3 (space-separated 0s and 1s): 1 0 0
   
   SAMPLE OUTPUT 1:
   The largest sub-square matrix containing all zeroes is:
   [0, 0]
   [0, 0]

   The largest value of the sub-square matrix contining all zeroes is:  4

   TEST CASE 2:
   SAMPLE INPUT 2:
   Enter the number of columns in the matrix: 5
   Enter row 1 (space-separated 0s and 1s): 1 0 1 0 1
   Enter row 2 (space-separated 0s and 1s): 0 0 1 0 1
   Enter row 3 (space-separated 0s and 1s): 1 1 0 0 0 
   Enter row 4 (space-separated 0s and 1s): 1 0 0 0 0
   Enter row 5 (space-separated 0s and 1s): 0 1 0 0 0

   SAMPLE OUTPUT 2:
   The largest sub-square matrix containing all zeroes is:
   [0, 0, 0]
   [0, 0, 0]
   [0, 0, 0]

   The largest value of the sub-square matrix contining all zeroes is:  9


   TEST CASE 3:
   SAMPLE INPUT 3:
   Enter the number of rows in the matrix: 9
   Enter the number of columns in the matrix: 9
   Enter row 1 (space-separated 0s and 1s): 1 1 0 0 0 0 0 1 0
   Enter row 2 (space-separated 0s and 1s): 0 0 0 0 0 0 0 1 1
   Enter row 3 (space-separated 0s and 1s): 0 0 0 0 0 0 0 1 0
   Enter row 4 (space-separated 0s and 1s): 1 1 0 0 0 0 0 1 1
   Enter row 5 (space-separated 0s and 1s): 1 0 0 0 0 0 0 1 0
   Enter row 6 (space-separated 0s and 1s): 1 0 1 0 0 1 0 1 0 
   Enter row 7 (space-separated 0s and 1s): 0 0 1 0 0 0 0 0 0
   Enter row 8 (space-separated 0s and 1s): 0 0 0 1 0 0 0 0 0
   Enter row 9 (space-separated 0s and 1s): 0 0 0 0 0 0 0 0 0

   SAMPLE OUTPUT 3:
   The largest sub-square matrix containing all zeroes is:
   [0, 0, 0, 0, 0]
   [0, 0, 0, 0, 0]
   [0, 0, 0, 0, 0]
   [0, 0, 0, 0, 0]
   [0, 0, 0, 0, 0]
   
   The largest value of the sub-square matrix contining all zeroes is:  25
   '''



def LSB(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    #IMPLEMENTATION OF DYNAMIC PROGRAMMING 
    dp = [[0] * (cols + 1) for i in range(rows + 1)]
    
    max_size = 0 #VARIABLE TO TRACK THE SIZE 
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == 0:
                #IF IT IS ZERO, UPDATE THE DYNAMIC MATRIX
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_size = max(max_size, dp[i][j])

    #EXTRACT THE SUBMATRIX WITH THE MAX SIZE
    sub_matrix = []
    for i in range(rows - max_size + 1, rows + 1):
        row = matrix[i - 1][cols - max_size:cols]
        sub_matrix.insert(0, row)

    return sub_matrix

#GETTING THE INPUT FROM THE USER 
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix = []
for i in range(rows):
    #ENTERING EACH ROW SEPERATELY WITH SPACE IN BETWEEN 
    row = list(map(int, input(f"Enter row {i + 1} (space-separated 0s and 1s): ").split()))
    matrix.append(row)
#CALLING THE FUNCITON 
result = LSB(matrix)
count = 0
for i in range(len(result)):
    for j in range(len(result)):
        result[i][j] = 0
        count+= 1
print("\nThe largest sub-square matrix containing all zeroes is:")
for row in result:
    print(row)
print("\n The largest value of the sub-square matrix contining all zeroes is: ",count)
