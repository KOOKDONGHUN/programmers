def solution(n):

    res = ""
    answer = ["4", "1", "2"]

    while(n):
        res = answer[int(n%3)] + res
        if (not(n%3)):
            n = int(n/3) -1
        else:
            n = int(n/3)
    print(res)
    return res
# reference
# https://mungto.tistory.com/206

# others solution
# def change124(n):
#     num = ['1','2','4']
#     answer = ""
#
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
#
#     return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution(1)
    solution(2)
    solution(3)
    solution(4)
