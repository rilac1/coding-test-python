from flask import Flask, request
import uuid
import random


app = Flask(__name__)
# 등록된 참가자마다 각 시도를 [auth_key: {answer, life}, ...] 형태로 저장
candidates = {
    'ABCDEFGH12345678': {}
}
flag = 'BINARY_SEARCH_KING'


@app.route('/start', methods=['GET'])
def create():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    # 현재 시도에 대한 대한 키(auth_key) 발급
    auth_key = str(uuid.uuid4())
    data = {
        'answer': random.randint(0, int(1e9)),
        'life': 35
    }
    candidates[access_token][auth_key] = data
    print(f'[New] {data}')
    # 클라이언트(client)에게 결과 반환
    return {
        'status': 'success',
        'auth_key': auth_key
    }


@app.route('/query', methods=['POST'])
def index():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    params = request.get_json()
    # auth_key가 올바르지 않을 때
    auth_key = params['auth_key']
    if auth_key not in candidates[access_token]:
        return {
            'status': 'unknown authentication key'
        }
    # 클라이언트(client)로부터 제출 받은 값
    if 'value' not in params:
        return {
            'status': 'value is needed'
        }
    value = params['value']
    # 목숨(life) 1만큼 감소
    candidates[access_token][auth_key]['life'] -= 1
    answer = candidates[access_token][auth_key]['answer']
    # 클라이언트에게 돌려 줄 값 설정
    if candidates[access_token][auth_key]['life'] < 0: result = "fail"
    elif value == answer: result = flag
    elif value < answer: result = 'up'
    else: result = 'down'
    return {
        'status': 'success',
        'result': result
    }


app.run(host="localhost", port=5000)
