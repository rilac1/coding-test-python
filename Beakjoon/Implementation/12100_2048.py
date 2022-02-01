# 2048
import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def up(b):
    for j in range(N):
        end = 0
        for i in range(1, N):
            if b[i][j]:
                temp, b[i][j] = b[i][j], 0
                if b[end][j]==0:
                    b[end][j] = temp
                elif b[end][j]==temp:
                    b[end][j] *= 2
                    end += 1
                else:
                    end += 1
                    b[end][j] = temp
    return b

def down(b):
    for j in range(N):
        end = N-1
        for i in range(N-1)[::-1]:
            if b[i][j]:
                temp, b[i][j] = b[i][j], 0
                if b[end][j]==0:
                    b[end][j] = temp
                elif b[end][j]==temp:
                    b[end][j] *= 2
                    end -= 1
                else:
                    end -= 1
                    b[end][j] = temp
    return b

def left(b):
    for i in range(N):
        end = 0
        for j in range(1, N):
            if b[i][j]:
                temp, b[i][j] = b[i][j], 0
                if b[i][end]==0:
                    b[i][end] = temp
                elif b[i][end]==temp:
                    b[i][end] *= 2
                    end += 1
                else:
                    end += 1
                    b[i][end] = temp
    return b

def right(b):
    for i in range(N):
        end = N-1
        for j in range(N-1)[::-1]:
            if b[i][j]:
                temp, b[i][j] = b[i][j], 0
                if b[i][end]==0:
                    b[i][end] = temp
                elif b[i][end]==temp:
                    b[i][end] *= 2
                    end -= 1
                else:
                    end -= 1
                    b[i][end] = temp
    return b

move = [up, right, down, left]
def back(b, n):
    global ans
    if n==5:
        ans = max(ans, max(map(max, b)))
    else:
        for i in range(4): 
            back(move[i](deepcopy(b)), n+1)

ans = 0
back(board,0)
print(ans)