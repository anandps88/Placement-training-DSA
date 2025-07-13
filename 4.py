n = int(input())
chessBoard = [[0 for _ in range(n)] for _ in range(n)]

def isattack(row, col):
    for i in range(row):
        if chessBoard[i][col] == 1:
            return True
    
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if chessBoard[i][j] == 1:
            return True
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if chessBoard[i][j] == 1:
            return True
        i -= 1
        j += 1
    return False

def nqueens(row):
    if row == n:
        return True
    for col in range(n):
        if not isattack(row, col):
            chessBoard[row][col] = 1
            if nqueens(row + 1):
                return True
            chessBoard[row][col] = 0
    return False

if nqueens(0):
    print("Possible")
else:
    print("Not Possible")

