#반복문(for문 & while문)

#for문: ~하는 동안 ==>  횟수에 의한 반복
'''
for 변수 in 범위: 
    실행구문
'''

#1~10까지의 정수를 출력
#1~n까지의 정수 range(1, (n+1), 1)
#for 변수 in range(시작값, 끝값, 단계)
#for num in range(1, 11, 1):
 #   print(f'{num} : hello')
    

#while문: ~하는 동안 ==>  조건에 의한 반복
# 0부터 10까지의 정수를 출력
#for num in range(0, 11, 1):
 #   print(f'num: {num}')

#range() 간략화 - 단계가 1인 경우 단계를 생략할 수 있다.
#for num in range(0, 11):
 #    print(f'num: {num}')
#단계가 생략되고 시작이 0이면 시작도 생략 가능
#for num in range(11):
 #   print(f'num: {num}')

#2~8 사이 짝수 출력

#for num in range(2, 9, 2):
    #print(f'num: {num}')

#for num in range(1, 16):
#   if (num <=8) and (num % 2 == 0):
#       print(f'num: {num}')

# 사용자가 입력한 횟수만큼 '메일발송!' 문자열 출력
#number = int(input('숫자를 입력하세요:'))
#for mail in range(number):
 #   print('메일발송!')

#1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기 
'''for num in range(1, 11):
    if num % 3 == 0:
       print('3의 배수!')
    else:
       print(num)
'''
#사용자가 원하는 구구단을 입력하면 해당 구구단을 출력하자
'''
userInputData = int(input('원하는 단을 입력하세요.'))
for num in range(1, 10):
   resultStr = f'{userInputData} X {num} = {userInputData * num}'
   print(resultStr)
'''
#1~10까지 정수의 합 출력하기
#sum = 0
#for i in range(1, 11):
 #   sum += i
#print(f'sum: {sum}')

#for문을 이용해서 1~100까지 정수 중에서
#3과 7의 공배수와 최소공배수를 출력하시오.
minNum = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 7 ==0:
        print(f'3과 7의 공배수: {num}')
        if minNum ==0: nimNum = num 

'''
지금까지 이터러블에 range 함수를 이용한 예를 살펴봤습니다.
이터러블에는 다음과 같이 문자열도 이용할 수 있습니다.
'''

for ch in 'hello':
    print(f'ch: {ch}')


#50보다 작은 7의 배수 출력
for num in range(1, 51):
    if num % 7 == 0:
        print(f'num: {num}')