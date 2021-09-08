def solution(s):
    answer = True

    op = 0

    for idx in range(len(s)):
        if (s[idx] == "("):
            op += 1
        elif (s[idx] == ")"):
            op -= 1

        if (op < 0):
            return False

    if (op == 0):
        return True
    else:
        return False

    return True

# others solution
# def is_pair(s):
#     # 함수를 완성하세요
#     x = 0
#     for w in s:
#         if x < 0:
#             break
#         x = x+1 if w=="(" else x-1 if w==")" else x
#     return x==0

if __name__ == "__main__":
    # execute only if run as a script
    solution("()()")
    solution("(())()")
    solution(")()(")
    solution("(()(")
