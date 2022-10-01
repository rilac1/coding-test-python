import requests, json

API_HOST = 'http://localhost:5000'
headers = {
    'Access-Token': 'ABCDEFGH12345678',
    'Content-Type': 'application/json'
}

def request(path, method, data={}):
    url = API_HOST + path

    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        # print(f'Sended data: {data}')
        return requests.post(url, headers=headers, data=json.dumps(data))


# auth_key를 발급 받고, 문제 풀이 시작
response = request('/start', 'GET')
data = response.json()
key = data['auth_key']

data = {
    "auth_key": key,
    "value": 0
}

def binary_search():
    left = 0
    right = 1000000000

    while left <= right:
        mid = (left + right) // 2
        data["value"] = mid

        r = request("/query", 'POST', data)
        json_data = r.json()

        result = json_data['result']
        if result == 'up':
            left = mid + 1
        elif result == 'down':
            right = mid - 1
        else:
            return result

print(binary_search())
