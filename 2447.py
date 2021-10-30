s = '*'
b = ' '
def star(N,i,j):
    print(s*N, end='')
    print()
    print(s*(N//3), end='')
    print(b*(N//3), end='')
    print(s*(N//3), end='')
    print()
    print(s*N, end='')
    print()
    
star(int(input()),0,0)


"""
*********
* *   * *
******* *
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
"""