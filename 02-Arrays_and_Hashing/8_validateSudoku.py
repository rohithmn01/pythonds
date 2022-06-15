
def validateSudoku(lis):
    i = 0
    col_lis=[]
    for line in lis:
        content = list(filter(lambda x : x!= '.',line))
        if len(content) != len(set(content)):
            return False
    rez = [[lis[j][i] for j in range(9)] for i in range(9)]
    for row in rez:
        content = list(filter(lambda x : x!= '.',row))
        if len(content) != len(set(content)):
            return False
    tri=[]
    for k in range(9):
        for i in range(k*3 % 9,k*3+3 %9):
            for j in range(3):
                if lis[i][j] != '.':
                    tri.append(lis[i][j])
        if len(tri) != len(set(tri)):
            return False
        print(tri)



res=validateSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])