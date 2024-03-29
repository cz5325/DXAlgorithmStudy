s = list(input())

def solution(s):
    answer = []
    min_answer = 1000000000
    for i in range(1, len(s)//2+1):
        new_li = []
        answer = []
        count = 1
        for num in range(0, len(s), i):
            new_li.append(s[num:num+i])
        for j in range(len(new_li)-1):
            if ''.join(new_li[j]) == ''.join(new_li[j+1]):
                count += 1
            else:
                if count == 1:
                    answer += new_li[j]
                else:
                    answer += list(str(count)) + new_li[j]
                count = 1
        if count == 1:
            answer += new_li[len(new_li)-1]
        else:
            answer += list(str(count)) + new_li[len(new_li)-1]
        if len(answer) < min_answer:
            min_answer = len(answer)
    return min_answer

print(solution(s))