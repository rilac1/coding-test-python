from collections import deque

class Card:
    def __init__(self, balance):
        self.__balance = balance
        self.__pay_q = deque()


    def deposit(self, k):
        self.__balance += k

        while self.__pay_q:
            if self.__check(self.__pay_q[0]):
                self.__balance -= self.__pay_q.popleft()
            else:
                break


    def pay(self, k):
        if self.__check(k):
            self.__balance -= k


    def reservation(self, k):
        if self.__check(k) and not self.__pay_q:
            self.__balance -= k
        else:
            self.__pay_q.append(k)


    def get_balance(self):
        return self.__balance


    def __check(self, k):
        return self.__balance >= k


N, M = map(int, input().split())
card = Card(N)

for _ in range(M):
    method, k = input().split()
    k = int(k)

    if method == 'deposit':
        card.deposit(k)
    elif method == 'pay':
        card.pay(k)
    elif method == 'reservation':
        card.reservation(k)

print(card.get_balance())