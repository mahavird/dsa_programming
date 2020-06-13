

def safe(maze,i,j):
    
    if not 0<=i<=len(maze)-1:
        return False
    if not 0<=j<=len(maze[0])-1:
        return False
    if maze[i][j] == 0:
        return False
    return True
    
total_path= []

def traverse_maze(maze,i,j,path):
    if i == n-1 and j == n-1 :
        #print("path",path)
        total_path.append(path)
        return
    
    #print("here",i,j)
    old_val = maze[i][j]
    maze[i][j] = 0

    if  safe(maze,i,j+1):
        path +="R"
        traverse_maze(maze,i,j+1,path)
        path = path[:-1]
    if  safe(maze,i,j-1):
        path+="L"
        traverse_maze(maze,i,j-1,path)
        path = path[:-1]
    if  safe(maze,i-1,j):
        path+="U"
        traverse_maze(maze,i-1,j,path)
        path = path[:-1]
    if  safe(maze,i+1,j):
        path+="D"
        traverse_maze(maze,i+1,j,path)
        path = path[:-1]
    maze[i][j] = 1
    
    





no_test = int(input())

#print("Test Cases",no_test)

matrix = []




for i in range(no_test):
    str1 = ""
    n = int(input())
    #print("size of matrix",n)
    string_matrix = input()
    #string_matrix = "1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1"
    #print(string_matrix)
    list_string  = (string_matrix.split(" "))
    list_string = list(map(int, list_string))
    #print(list_string)

    matrix = [list_string[i:i+n] for i in range(0,len(list_string),n)]
    """ for i in range(n):
        matrix.append([])
        data[i:i+n-1]
        print(matrix)
        for j in range(n):
            matrix[i].append(int(list_string[i+j])) """
    #print(matrix)
    traverse_maze(matrix,0,0,"")
    #print(total_path)
    str1 = ' '.join(total_path)
    print(str1)
    total_path = []

