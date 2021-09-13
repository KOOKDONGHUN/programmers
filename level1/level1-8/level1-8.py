def solution(s):
    answer = 0

    dictionary = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for k, v in dictionary.items():
        if (k in s):
            s = s.replace(k, v)

    answer =int(s)

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution("one4seveneight")
    solution("23four5six7")
    solution("2three45sixseven")
    solution("123")