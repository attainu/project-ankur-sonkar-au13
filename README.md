MAZE PROBLEM:-

Objective:-

-> The maze is in matrix form, where 1's are the path and 0's are the blocked path.
-> The main goal of the maze problem is to find the shotest path from source to destination. If there is no
    path available it returns -1.

Concept Used:- 

1. Backtracking.
2. File handing.

Approch :-

-> Given a maze in which two points are source and destination and have to find the shortest path between them.
-> The maze is given in the form of matrix which is NxN matrix.
-> The source of the maze is [0][0] and the destination is [n - 1][n - 1].
-> While traveling from the path there are blocks in between which are denoted by 0's and the path in which we can move is 
    denoted by 1's.
-> As we go through the path following the 1's and reach the destination we give the output (or) if there is no path we return 
    "-1"

Algorithem:-

-> Create a solution matrix, initially filled with 0’s.
-> Create a recursive funtion, which takes initial matrix, output matrix and position (i, j).
-> If the position is out of the matrix or the position is not valid then return.
-> Mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.
-> Recursively call for position (i+1, j) and (i, j+1).
-> Unmark position (i, j), i.e output[i][j] = 0.


Input:-

-> Open the folder in VS Code.
-> Open the file inputfile.txt
-> Enter a square matrix.

Output:- 

-> Open the file outputfile.txt
-> If the given matrix has the path the output is show in shotest path (or) it returns -1.


Sample Input and Output:

Sample Input:-

5
1 0 0 0 0
1 1 0 0 0
0 1 1 0 0
0 0 1 1 0
1 1 1 1 1

Sample Output:- 

1 0 0 0 0
1 1 0 0 0
0 1 1 0 0
0 0 1 0 0
0 0 1 1 1