n = int(input()) #정수 N 입력 받기
array = list(map(int, input().split())) #모든 식량정보 입력받기

d = [0]* 100 #앞서 계산된 결과를 저장하지 않기 위해서

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])
##################################바텀업방식
