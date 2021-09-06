import re

def solution(new_id):
    answer = ''
    print(f"원본 ::: [{new_id}]")

    # 1. 소문자 치환
    new_id = new_id.lower()
    print(f"소문자 치환 ::: [{new_id}]")

    # 2. [알파벳 소문자, 숫자, -, _, .]를 제외한 모든 문자 제거
    regex = re.compile('[^a-z0-9-_.]')
    new_id = regex.sub("", new_id)
    print(f"[알파벳 소문자, 숫자, -, _, .] 이외 제거 ::: [{new_id}]")

    # 3. 연속된 마침표는 하나로 치환 (level2-1 문자열 압축 참고)
    res = ''
    for i in range(1, 2):
        cnt = 1
        t = new_id[:i]
        for j in range(i, len(new_id), i):
            if (new_id[j:j+i] == t == '.'):
                cnt += 1
            else:
                if cnt == 1:
                    res += t
                else:
                    res += '.'
                t = new_id[j:j+i]
                cnt = 1

        res += t
    new_id = res
    print(f'연속 마침표 치환 ::: [{new_id}]')

    # 4. 마침표가 처음이나 마지막인경우 제거
    if (len(new_id) == 1):
        if (new_id[0] == '.'):
            new_id = ''
    elif (len(new_id) == 2):
        if (new_id[0] == '.' and new_id[-1] == '.'):
            new_id = ''
        elif(new_id[0] == '.'):
            new_id = new_id[1]
        elif(new_id[-1] == '.'):
            new_id = new_id[0]
    else:
        if (new_id[0] == '.' and new_id[-1] == '.'):
            new_id = new_id[1:-1]
        elif(new_id[0] == '.'):
            new_id = new_id[1:]
        elif(new_id[-1] == '.'):
            new_id = new_id[:-1]
    print(f'마침표가 처음 또는 마지막 제거 ::: [{new_id}]')

    # 5. new_id가 빈 문자열인 경우 a
    if (new_id == ''):
        new_id = 'a'
    print(f'빈 문자열의 경우 a ::: [{new_id}]')

    # 6. 길이 16이상 첫글자 부터 15글자로 자르고 마지막이 . 일 경우 마지막 제거
    if (len(new_id) >= 16):
        new_id = new_id[:15]
        print(f"15자 이상이라서 줄임 ::: [{new_id}]")
        if (new_id[-1] == '.'):
            new_id = new_id[:-1]
    print(f'글자 15자 이내로 줄이고 마지막 . 제거 ::: [{new_id}]')

    # 7. 2글자 이하의 경우 마지막 문자를 길이가 3이 될때 까지 반복
    if (len(new_id) <= 2):
        t = new_id[-1]
        while(len(new_id) < 3):
            new_id += t
    print(f'2글자 이하의 경우 마지막 문자를 길이가 3이 될때 까지 반복 ::: [{new_id}]')

    answer = new_id
    print('-' * 33)
    return answer

# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

if __name__ == "__main__":
    # execute only if run as a script
    solution("...!@BaT#*..y.abcdefghijklm")
    solution("z-+.^.")
    solution("=.=")
    solution("123_.def")
    solution("abcdefghijklmn.p")