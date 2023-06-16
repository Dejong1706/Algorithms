T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = A*B

    while B>0:
        A,B = B, A%B

    print(result//A)

# 최소공배수는 두 변수의 곱에 최대 공약수를 나누어 주면 된다
# 최대 공약수 구하는법 두번째 변수가 0이 될때까지 A = b, B = a%b를 대입(유클리드 호제법)