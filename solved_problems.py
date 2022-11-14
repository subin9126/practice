# 10926
# 80ms
name = input()
print(name + "??!")

# 88ms
import sys
name = sys.stdin.readline()
print(name[:-1] + "??!")

#-----------------------------------------
#18108
year = int(input())
print(str(year - 543))

#-----------------------------------------
#3003
#68ms
pieces = list(map(int, input().split()))
k = 1 - pieces[0]
q = 1 - pieces[1]
r = 2 - pieces[2]
b = 2 - pieces[3]
kn = 2 - pieces[4]
p = 8 - pieces[5]
print(k,q,r,b,kn,p, end=" ")

# 68ms
pieces = list(map(int, input().split()))
total = [1,1,2,2,2,8]

for i in range(6):
    print(total[i] - pieces[i], end = " ")

#-----------------------------------------
#10430
A,B,C = map(int, input().split())
print( (A+B)%C )
print( ((A%C) + (B%C))%C )
print( (A*B)%C )
print( ((A%C) * (B%C))%C )

#-----------------------------------------
# 2588
n1 = int(input())
n2 = input()

n3 = n1 * int(n2[-1])
n4 = n1 * int(n2[1])
n5 = n1 * int(n2[0])
print(n3)
print(n4)
print(n5)
print( n3 + (n4*10) + (n5*100))

'''
2 - 조건문 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
# 1330
A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")

# 9498
score = int(input())
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

# 2753
year = int(input())

# 4의 배수이면
if year % 4 == 0:
    #100의 배수 아니거나 400의 배수이면
    if year % 100 > 0 or year % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)

#14681
#72 ms
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    else:
        print(3)

#72 ms
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)

# 2884
H, M = map(int, input().split())

#45분 일찍 돌리기
newM = M - 45
if newM < 0:
    newM = 60 + newM
    newH = H - 1

    if newH < 0:
        newH = 24 + newH

else:
    newH = H

print(newH, newM)

# 2525 *************************왜 틀리는지 모르겠음 ㅜㅜㅜㅜㅜ
H, M = map(int, input().split())
cook = int(input())

# cook 시간이 1시간 넘을 수 있음.
# 예. 271분이면 cook_h = 4, cook_m = 31, 4시간 31분.
# 예. 80분이면 cook_h = 1, cook_m = 20, 1시간 20분.
# 예. 20분이면 cook_h - 0, cook_m = 20, 20분.
cook_h = cook // 60
cook_m = cook % 60

newM = M + cook_m
if newM >= 60:
    newM = newM - 60

    newH = H + cook_h + 1
    if newH >= 24:
        newH = newH - 24

else:
    newH = H + cook_h

print(newH, newM)

# 2480
a, b, c = map(int, input().split())

if a == b == c:
    prize = 10000 + a*1000
else:
    order = sorted([a,b,c])
    if order[0] == order[1] or order[1] == order[2]:
        prize = 1000 + order[1]*100
    else:
        prize = order[2]*100

print(prize)

'''
3 - 반복문 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
# 2739
N = int(input())
for i in range(1,10):
    print("{} * {} = {}".format(N, i, N*i))

# 10950
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(A+B)

# 8393
#76ms
n = int(input())
tot = 0
for i in range(1, n+1):
    tot += i
print(tot)

#80ms
n = int(input())
tot = sum(range(1, n+1))
print(tot)


# 25304
X = int(input())
N = int(input())

tot = 0
for i in range(N):
    x, n = map(int, input().split())
    tot += x*n

if X == tot:
    print("Yes")
else:
    print("No")

# 15552
import sys
T = int(input())
for tc in range(T):
    # for문 안에 입력방식이 느리면 시간초과날수있음 ***********************
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# 11021
import sys
T = int(input())
for tc in range(1, T+1):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(tc, A+B))

# 11022
import sys
T = int(input())
for tc in range(1, T+1):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(tc, A, B, A+B))

# 2438
n = int(input())
for i in range(1, n+1):
    print( '*' * i)

# 2439 ****************** 중요!!
n = int(input())
for i in range(1, n+1):
    # 공백과 * 사이에 공백이 하나 더 들어간다
    # 공공공공 별
    #print(' '*(n-i), '*' * i)

    #아래처럼 해야 공백과 별이 붙고 출력형식 오류가 안 생긴다
    # 공공공공별
    print(' '*(n-i) + '*'*i)


# 10952 - WHILE TRUE의 용도를 알 수 있음 ***********************************************************
import sys

#test case수가 정의되지 않은 문제.
#0 0이 입력되는 순간 멈춘다.
#특혈한 일이 없는 한 계속 반복문 진행하라 -> while True:
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    print(A+B)

# 10951 *************************************EOF를 알 수 있는 문제
#test case수가 정의되지 않은 문제.
#종결규칙도 없음. 단순히 EOF(end of file)일 때 끝나는건데.
#아무것도 입력 안할 때 (A,B입력안하고 Enter만 칠 때)
import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break

#아래대로 하면 런타임 에러 발생; 왜?
import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except EOFError:
        break

#또다른 방법 (맞다고 함. 파이참에선 잘 안됨)
import sys
lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.split())
    print(A+B)


# 1110 ---- 이 문제 뭐임 ㅡ.ㅡ [SKIP]
N = input()  # 26

#두자리 수 input
if int(N) < 10:
    N = N + 0

a = int(N[0]) + int(N[1]) # 2 + 6 = 8
b = N[1] + a # 6 + 8 = 14
str(a[-1])

'''
4 - 1차원 배열
'''
# 10807
N = int(input())
arr = list(map(int, input().split()))
x = int(input())

num = 0
for i in arr:
    if i == x:
        num += 1
print(num)

# 10871
N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in A:
    if i < X:
        ans.append(i)
print(*ans)

# 10818 *******shows that updating min/max through 1 loop is faster than sorting and finding min/max ********
N = int(input())
arr = list(map(int, input().split()))

#496ms
print(min(arr), max(arr))

#776ms
arr.sort()
print(arr[0], arr[-1])

#480ms
min_n = arr[0]
max_n = arr[0]
for a in arr:
    if a < min_n:
        min_n = a
    if a > max_n:
        max_n = a
print(min_n, max_n)

# 2562
import sys

max_i = 0
max_num = 0
for i in range(9):
    curr_num = int(sys.stdin.readline())
    if curr_num > max_num:
        max_num = curr_num
        max_i = i
print(max_num)
print(max_i+1)

# 5597
import sys
student_list = list(range(1,31))
for i in range(28):
    student_num = int(sys.stdin.readline())
    student_list[student_num-1] = False

n = 0
for a in student_list:
    if n > 3:
        break
    if a is not False:
        print(a)
        n += 1

# 3052
import sys
ans = set()
for i in range(10):
    a = int(sys.stdin.readline())
    ans.add(a % 42)

print(len(ans))

# 1546
import sys
N = int(input())

def convert(raw, highest):
    return(raw/highest*100)

tot = 0
scores = list(map(int, sys.stdin.readline().split()))

for s in scores:
    tot += convert(s, max(scores))

print(tot/N)

# 8598
import sys
T = int(input())
for tc in range(1, T+1):
    case = list(sys.stdin.readline().rstrip())

    result = 0
    consec = 0
    for c in case:
        if c == 'O' and consec == 0:
            consec = 1
            result += consec
        elif c == 'O' and consec > 0:
            consec += 1
            result += consec
        elif c == 'X':
            consec = 0

    print(result)

# 4344
import sys
C = int(input())
for tc in range(1, C+1):
    scores = list(map(int, sys.stdin.readline().split()))
    student_num = scores.pop(0)
    #leftover nums will be student scores.

    avg = sum(scores)/student_num
    higher_than_avg = 0

    for s in scores:
        if s > avg:
            higher_than_avg += 1

    print("{:.3f}".format(higher_than_avg/student_num*100) + "%")


'''
5 - 함수
'''
# 15596 ******* def의 input과 output type을 지정할 수 있다 *****************************

def solve(a: list) -> int:
    return sum(a)

# 4673
#생성자가 있는 숫자인지 확인
def generate_next_num(a: int) -> int:
    next_num = a
    for i in range(len(str(a))):
        next_num += int(str(a)[i])
    return next_num

# 1부터 10000의 숫자들.
arr = [False for _ in range(10000)]

for n in range(1,10001):
    has_gen = generate_next_num(n)
    if has_gen < 10000:
        arr[has_gen-1] = True   #mark generated number as True (has a generator == not self number)
                                # zero-indexing이기 때문에 generated number에서 1 빼기
# False로 남아있는 숫자들은 generator 없으므로 self number들임.
for n in range(10000):
    if arr[n] is False:
        if n+1 < 10000:
            print(n+1)

'''
6 - 문자열
'''

'''
7 - 2차원 배열
'''
# 2738
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
    print(*C[i])

# 2566
arr = [ list(map(int, input().split())) for _ in range(9)] #<-sys.stdin.readline으로 해도 걸리는 시간은 똑같음;

max_val = 0
max_xy = [0,0]

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_xy = [i, j]

print(max_val)
print(max_xy[0]+1, max_xy[1]+1)

# 2563
N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0

def overlay_paper(i,j):
    cnt = 0
    for ni in range(i, i+10):
        for nj in range(99-j-10, 99-j):
            arr[nj][ni] += 1
            if arr[nj][ni] == 1:
                cnt += 1
                print(cnt)
                #if first time filling this, include in count.
                # else, have already included this in count from other paper.
    return arr, cnt

tot = 0
for n in range(N):
    x, y = map(int, input().split())
    overlay_paper(x,y)
    tot += cnt

print(tot)


