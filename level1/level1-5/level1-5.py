def solution(a, b):
    answer = 0

    if (b >= a):
        s = [c for c in range(a, b + 1)]
    elif (b <= a):
        s = [c for c in range(b, a + 1)]

    answer = sum(s)

    return answer

# others solution
# def solution(a, b):
#     # 함수를 완성하세요
#     if a > b: a, b = b, a
#
#     return sum(range(a,b+1))

if __name__ == "__main__":
    # execute only if run as a script
    solution(3,5)
    solution(3,3)
    solution(5,3)