# def solution(s):
#     min = float("inf")
#     offset = 1
#     answer = len(s)
#
#     if (len(s) == 1):
#         answer = 1
#     elif (len(s) == 2):
#         answer = 2
#     else:
#         while (offset <= len(s)/2):
#             answer = ""
#             t = s[:offset]
#             print(t)
#             cnt = 1
#             for i in range(offset, len(s) - offset, offset):
#                 p = s[i:i+offset]
#                 print(p)
#                 if (t == p):
#                     cnt += 1
#                 else :
#                     if(cnt > 1):
#                         answer += str(cnt)
#                     answer += t
#                     t = p
#                     cnt = 1
#             answer += s[i:]
#             if (len(answer)  < min):
#                 min = len(answer)
#
#             offset += 1
#         answer = min
#         print(answer)
#     return answer

# copy from https://velog.io/@devjuun_s/%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python2020-Kakao-%EA%B3%B5%EC%B1%84
def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        print(result)
        result = ""
    return min(length)


if __name__ == "__main__":
    # execute only if run as a script
    solution("aabbaccc")
    print('-'*30)
    solution("ababcdcdababcdcd")
    print('-'*30)
    solution("abcabcdede")
    print('-' * 30)
    solution("abcabcabcabcdededededede")
    print('-' * 30)
    solution("xababcdcdababcdcd")