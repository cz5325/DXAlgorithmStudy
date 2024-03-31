data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  # 숫자인 경우 변수에 저장
  if x.isdigit() :
    value += int(x)
  # 알파벳인 경우 리스트에 삽입
  else :
    result.append(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))


# 최종결과출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))


# isalpha(): 알파벳인지 확인
# isdigit(): 숫자인지 확인

