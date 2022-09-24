# UNION-FIND
parent = {}
for n in range(1, 51):
    for m in range(1, 51):
        parent[(n, m)] = (n, m)

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# Main Logic
graph = [['EMPTY'] * 51 for _ in range(51)]

def solution(commands):
    answer = []

    for command in commands:
        argv = command.split()

        if argv[0] == 'UPDATE':
            if len(argv) == 4:
                update(argv)
            else:
                rename(argv)
        elif argv[0] == 'MERGE':
            merge(argv)
        elif argv[0] == 'UNMERGE':
            unmerge(argv)
        elif argv[0] == 'PRINT':
            answer.append(result(argv))

    return answer

def update(argv):
    r, c, = map(int, argv[1:3])
    value = argv[-1]

    parent_r, parent_c = find((r, c))
    graph[parent_r][parent_c] = value

def rename(argv):
    value1, value2 = argv[1:]
    for i in range(1, 51):
        for j in range(1, 51):
            if graph[i][j] == value1:
                graph[i][j] = value2

def merge(argv):
    r1, c1, r2, c2 = map(int, argv[1:])
    parent_r1, parent_c1 = find((r1,c1))
    parent_r2, parent_c2 = find((r2,c2))

    if (graph[parent_r1][parent_c1]) == 'EMPTY':
        graph[parent_r1][parent_c1] = graph[parent_r2][parent_c2]

    union((r1, c1), (r2, c2))
    return -1

def unmerge(argv):
    r, c = map(int, argv[1:])
    parent_r, parent_c = find((r, c))
    original_value = graph[parent_r][parent_c]

    for key in parent.keys():
        if find(key) == (parent_r, parent_c):
            parent[key] = key
            graph[key[0]][key[1]] = 'EMPTY'

    graph[r][c] = original_value

def result(argv):
    r, c = map(int, argv[1:])
    parent_r, parent_c = find((r, c))
    return graph[parent_r][parent_c]


cmd = ["UPDATE 1 1 menu",
       "UPDATE 1 2 category",
       "UPDATE 2 1 bibimbap",
       "UPDATE 2 2 korean",
       "UPDATE 2 3 rice",
       "UPDATE 3 1 ramyeon",
       "UPDATE 3 2 korean",
       "UPDATE 3 3 noodle",
       "UPDATE 3 4 instant",
       "UPDATE 4 1 pasta",
       "UPDATE 4 2 italian",
       "UPDATE 4 3 noodle",
       "MERGE 1 2 1 3",
       "MERGE 1 3 1 4",
       "UPDATE korean hansik",
       "UPDATE 1 3 group",
       "UNMERGE 1 4",
       "MERGE 1 3 1 4",
       "PRINT 1 3"
       ]
a = solution(cmd)
for i in range(1,5):
    print(graph[i][1:5])
print("a:", a)