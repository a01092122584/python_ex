#369 게임 만들기
'''
1부터 99까지 1씩 증가하면서 숫자에 3, 6, 9가 들어 있을 때마다 숫자와 함께
'짝!'을 출력합니다.
'''
for num in range(1, 100):

    # 한 자리 수
    if num <= 9:
        if num % 3 == 0:
            print(f'{num}, 짝!')
        else:
            print(f'{num}')

    # 두 자리 수
    else:
        printStr = str(num)
        print(f'{num}')

        firstNum = num // 10
        secondNum = num % 10

        if firstNum % 3 == 0:
            print('짝!')
            printStr += ', 짝!'

        if secondNum % 3 == 0 and secondNum != 0:
            print('짝!')
            printStr += ', 짝!'
        
        print(f'{printStr}')

# 열차 교차 시간 알아내기 
'''
대전역에는 3개 노선의 열차가 오전 9시부터 오후 6시까지 교차 운행한다.
3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막으세요.
단 매일 오전 9시에 대전역에서 모든 열차가 출발한다.

a 열차 : 첫차 오전 9시   마지막 차 오후 6시   운행 간격 10분
b 열차 : 첫차 오전 9시   마지막 차 오후 6시   운행 간격 25분
c 열차 : 첫차 오전 9시   마지막 차 오후 6시   운행 간격 30분
'''

trainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB <-> trainC')
        #print(9 + n // 60, end='')           #시
        #print('시', end='')
        #print(n % 60, end='')                #분
        #print('분')
        print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainA == 0 and n % trainB == 0:
        print('trainA <-> trainB')
        #print(9 + n // 60, end='')           #시
        #print('시', end='')
        #print(n % 60, end='')                #분
        #print('분')
        print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        #print(9 + n // 60, end='')           #시
        #print('시', end='')
        #print(n % 60, end='')                #분
        #print('분')
        #print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainA == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        #print(9 + n // 60, end='')           #시
        #print('시', end='')
        #print(n % 60, end='')                #분
        #print('분')
        print(f'{9 + n // 60}시 {n % 60}분')

#로그인 기능 만들기
'''
관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면 '암호를 다시 확인하세요!'를 출력하고
다시 암호를 물어봅니다.
5회 이상 로그인에 실패하면 '로그인 실패!! 횟수 초과!!!' 메시지를 출력하고 종료합니다.
암호가 올바르다면 '로그인 됐습니다.'를 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다.
'''

# ADMIN_PW = 'dwac1234'
# count = 1 
# while True:

#     if count > 5:
#         print('누구야~~ 로그인 실패!!')
#         break
#     inputPw = input('관리자 암호를 입력하세요.')

#     if inputPw != ADMIN_PW:
#         print('X --> 암호를 다시 입력하세요.')
#         count += 1
#     elif inputPw == ADMIN_PW:
#         print('O --> 로그인 성공!!')
#         break

'''
사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만드시오
팩토리얼은 1부터 양의 정수 n까지의 모든 정수를 곱한 값을 말한다
'''

# userInputIntegerData = int(input('양수 입력: '))
# result = 1
# for num in range(1, userInputIntegerData + 1):
#     result *= num 
# print(f'{userInputIntegerData}의 팩토리얼은 {result}이다')

# 숫자 맞추기 게임
'''
0부터 100사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오
요구사항
1부터 100까지의 난수를 발생시킨다
사용자가 입력한 숫자가 난수와 일치하면 '정답입니다.'를 출력하고 게임 종료
일치하지 않으면 '틀렸습니다. 다시 입력하세요.' 출력
기회는 10회로 제한 열 번을 넘어가면 '게임에 졌습니다.'를 출력하고 게임을 종료한다.
틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다.
'''
# import random
# randomNum = random.randint(1, 100)

# userNum = int(input('1~100의 숫자를 입력하세요. '))
# count = 1
# while True:
#     if randomNum == userNum:
#         print('정답입니다.')
#         break

#     elif randomNum < userNum:
#         print('틀렸습니다. 다시 입력하세요.DOWN ')
#     elif randomNum > userNum:
#         print('틀렸습니다. 다시 입력하세요.UP')
    
    
#     userNum = int(input('1~100의 숫자를 입력하세요. '))
#     count += 1
    
#     if count > 10:
#         print('게임에 졌습니다.')
#         break
# print(randomNum)

#가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램
'''
가로 길이는 1부터 2의 배수로 증가한다. (1,2,4.6,8...)
세로 길이는 1부터 3의 배수로 증가한다. (1,3,6,9,12...)
사각형의 넓이가 150보다 크면 프로그램을 종료한다.
가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''
#초기값
width = 1
height = 1
#가장 작은 넓이
minArea = width * height
#가장 큰 넓이
maxArea = width * height

while True:
    area = width * height # 사각형 넓이

    if area > 150:
        break
    print(f'가로: {width}, 세로: {height}, 넓이: {area}')

    if area < minArea:    #최소 넓이
        minArea = area

    if area > maxArea:    #최대 넓이
        maxArea = area

    if width == 1: #width가 1인 경우
        width = 2 
    else:          #width가 1인 아닌경우
        width += 2

    if height == 1: #width가 1인 경우
        height = 3 
    else:          #width가 1인 아닌경우
        height += 3
print(f'가장 작은 넓이: {minArea}')
print(f'가장 큰 넓이: {maxArea}')


    

