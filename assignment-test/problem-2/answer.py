import requests, json

API_HOST = 'http://localhost:5000'
headers = {
    'Access-Token': 'ABCDEFGH12345678',
    'Content-Type': 'application/json'
}

def request(path, method, data={}):
    url = API_HOST + path

    print(f'Request URL: {url}')
    print(f'HTTP Method: {method}')
    print(f'Headers: {headers}')

    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        print(f'Sended data: {data}')
        return requests.post(url, headers=headers, data=json.dumps(data))

def game():
    win_stacks = 0
    while win_stacks <= 30:
        board = [['_']*3 for _ in range(3)]
        response = request('/start', 'GET')
        json_data = response.json()
        key = json_data['auth_key']

        data = {
            'auth_key': key
        }

        # Start game
        while True:
            if 'result' in json_data:
                result = (json_data['result'])
                if result == 'computer win':
                    win_stacks = 0
                    break
                elif result == 'player win' or result == 'draw':
                    win_stacks += 1
                    break
                else:
                    return result
            else:
                if json_data['position'] != 'none':
                    x = int(json_data['position'][1])
                    y = int(json_data['position'][-2])
                    board[x][y] = 'X'

                x,y = defense(board)
                data['position'] = '(' + str(x) + ',' + str(y) + ')'
                response = request('/start', 'POST', )
                json_data = response.json()


visited = [[False]*3 for _ in range(3)]
def defense(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'X' and not visited[x][y]:
                visited[x][y] = True
                for d in range(6):
                    next = dfs(x,y,1,d,board)
                    if next:
                        return next
                visited[x][y] = False

    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                return x,y


def dfs(x,y,cnt,d,board):
    dx = [-1,0,1,0,1,-1]
    dy = [0,1,0,-1,1,-1]

    nx = x + dx[d]
    ny = y + dy[d]

    if not (0 <= nx < 3 and 0 <= ny < 3):
        return

    if cnt == 2:
        if board[nx][ny] == '_':
            return nx,ny

    if board[nx][ny] == 'X':
        dfs(nx,ny,2,d,board)

game()