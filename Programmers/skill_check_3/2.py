from collections import deque

def solution(begin, target, words):
    visited = {word: False for word in words}

    if target not in visited:
        return 0

    q = deque([(begin, 0)])
    while q:
        now, cnt = q.popleft()

        if now == target:
            return cnt

        for word in words:
            if not visited[word] and is_convertible(now, word):
                visited[word] = True
                q.append((word, cnt+1))

    return 0

def is_convertible(s1, s2):
    diff_count = 0

    for w1, w2 in zip(s1, s2):
        if w1 != w2:
            diff_count += 1
        if diff_count > 1:
            return False

    return True