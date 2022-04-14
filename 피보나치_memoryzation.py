################################Top-down방식
d = [0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] !=0:
         return d[x]
    d[x] = fibo(x-1)+fibo(x-1)
    return d[x]

fibo(6)

#################################Bottom-up방식(많이 쓰임)
d = [0]*100
d[1] =1
d[2] =1
n=99

for i in range(3,n+1):
    d[i] = d[i-1]+d[i+2]

print(d[n])

#################O(2^n)이 걸리는 게 O(N)의 공간 복잡도를 가짐
#################다이내믹 프로그래밍인지 여부판단 중요