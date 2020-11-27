import linecache
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", default = "inputfile.txt", help = "Enter Input File")
    parser.add_argument("-o", default = "outputfile.txt",help = "output will be provided in this file")
    input_file = open("inputfile.txt", "r")
    output_file = open("outputfile.txt", "w")
    A = linecache.getline("inputfile.txt", 1) #to get first line of input
    A = int(A)
    input_file = open("inputfile.txt", "r")
    input_file = open("inputfile.txt", "r")
    input_matrix = []
    for i in range(A + 1):
        line = input_file.readline()
        if i > 0:
            input_matrix.append(list(map(int, line.rstrip().split())))
    input_file.close()
    temporary_list = output_matrix(input_matrix, A)
    if type(temporary_list) is list:
        for i in temporary_list:
            for j in i:
                output_file.write(str(j))
                output_file.write(" ")
            output_file.write("\n")
        output_file.close()
    else:
        output_file.write(str(temporary_list))
        output_file.close()


# function for checking if x, y is vaild index for squre matrix
def valid_matrix(maze, x, y, A):
    if x >= 0 and x < A and y >= 0 and y < A and maze[x][y] == 1:
        return True
    return False


# this function returns the output either matrix or -1
def output_matrix(maze, A):
    sol = [[0 for j in range(A)] for i in range(A)]
    if not bt_maze(maze, 0, 0, sol, A):
        return "-1"
    return sol


# this function solves the maze problem using backtracking
def bt_maze(maze, x, y, sol, A):
    if x == A - 1 and y == A - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if valid_matrix(maze, x, y, A):
        sol[x][y] = 1
        if bt_maze(maze, x + 1, y, sol, A):
            return True
        if bt_maze(maze, x, y + 1, sol, A):
            return True
        sol[x][y] = 0 
        return False


if __name__ == "__main__":
    main()




