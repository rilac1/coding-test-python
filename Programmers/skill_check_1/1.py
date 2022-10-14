words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def solution(s):
    for i in range(10):
        s = s.replace(words[i], str(i))

    return s
