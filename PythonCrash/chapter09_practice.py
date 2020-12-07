"""
1)    ∑𝑛𝑘=1𝑘  을 계산하는 함수 sigma(n) 을 작성하라. (n 은 정수)
"""
def sigma(n):
    k = list(range(1, n+1))
    return sum(k)


print(sigma(10))

"""
Slide Type
2) 다음 문장 수행 후의 output 은 ?
"""
s = ("a", "b", "c")
for i in range(1, len(s) + 1):
    sub = ""
    for j in range(i):
        sub = s[j] + sub
    print(sub)
#%%
"""
3) 다음 문장 수행 후의 output 은 ?
"""
def sum_part(xlist, n):
    sum = 0
    for x in xlist[n]:
        sum = sum + x
    return sum

ylist = [[1, 2], [3, 4], [5, 6], [7, 8]]
x = sum_part(ylist, 2)
print(x)
#%%
"""
Slide Type
4) 숫자로 피라미드 만들기 : 홀수 숫자를 입력으로 받아서 좌우 대칭되는
피라미드형태로 출력 한다.
"""
def pyramid(n):
    for i in range(n):
        print(" " * (n - i), end="")
        for j in range(1, i + 2):
            print(j, end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()
pyramid(7)
#%%
"""
5) 임의의 범위의 숫자를 모두 곱하는 함수를 작성하라.
    ex) multiply(2,4) ==> 2 * 3 * 4 = 24
"""
def multiply(x, y):
    result = 1
    for i in range(x, y+1):
        result = result * i
    return result

print(multiply(2, 4))

"""
6) 숫자로 이루어진 list 의 평균을 구하는 함수를 작성하라.
   단, built-in 함수를 이용하지 않고 for loop 을 이용하여 새로운 함수 작성.
"""
def average(lst):
    sum = 0
    for n in lst:
        sum += n
    return sum / len(lst)

print(average([2,3,4,5,6]))
#%%
"""
7) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 을 for 문을 이용하여,

[1,2,3] , 4
[2,3,4] , 5
[3,4,5] , 6
[4,5,6] , 7
[5,6,7] , 8
[6,7,8] , 9
[7,8,9] , 10 을 출력하라
"""
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(x)-3):
    print(x[i:i+3], ',', x[i+3])
#%%
"""
>>도전문제
피보나치 수열(Fibonacci Sequence)을 계산하는 프로그램도 파이썬으로 간단히 작성할 수
있다.

피보나치 수열은 0 과 1 로 시작하고 다음의 숫자는 이전 숫자 두개를 더한 숫자들로
이루어 진다.
0, 1, 1, 2, 3, 5, 8, 13 ......

n 개의 숫자로 이루어진 피보나치 수열을 출력하는 함수를 작성하라.
"""
def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

lst = []
for i in range(10):
    lst.append(fib(i))

print(lst)
