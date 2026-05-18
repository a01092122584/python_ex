print('회원정보를 입력하세요.')

userName = input('이름: ')
userMail = input('메일: ')
userId = input('아이디: ')
userPw = input('비밀번호: ')

print('------------')
print('To. ' + userMail)
print('▶아이디 및 비밀번호 확인')
print(userName + '고객님 안녕하세요.')
print(userName + '고객님의 아이디와 비밀번호는 아래와 같습니다.')
print('아이디:' + userId)
print('비밀번호:' + userPw)
print('감사합니다.')
print('Naver 담당자')
print('------------')

userMail = 'gildong@gmail.com'
print('To. ' + userMail)
print('To. ' + userMail)

korScore = input('국어점수')
engScore = input('영어점수')
mathScore = input('수학점수')

print(f'국어 점수 : {korScore}')
print(f'영어 점수 : {engScore}')
print(f'수학 점수 : {mathScore}')
      
firstNum = int(input('첫 번째 정수 입력: '))
secondNum = int(input('두 번째 정수 입력:'))

print(f'합: {firstNum + secondNum}')
# print(f'평균:({firstNum + secondNum}' / 2)

var1 = 10
var2 = 20

print(f'var1: {var1}, var2: {var2}')

temp = var1
var1 = var2
var2 = temp
print(f'var1: {var1}, var2: {var2}')

