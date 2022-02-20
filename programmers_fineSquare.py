import math

def solution(w,h):
    answer = 1
    answer = w*h - (w+h-math.gcd(w,h))
    return answer
