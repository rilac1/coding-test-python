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


# auth_key를 발급 받고, 문제 풀이 시작
response = request('/start', 'GET')
print(f'Response status: {response.status_code}')

data = response.json()
print(f'Response: {data}')

key = data['auth_key']
print("auth_key:", key)
