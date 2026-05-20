#딕셔너리
#딕셔너리란, 파이썬에서 묶음 데이터를 관리하기 위한 컨테이너 자료형 중 하나이다. 
#키(key):벨류(value) 로 데이터를 관리합니다. 이 말은 딕셔너리에는 인덱스가 존재하지 않습니다.
# members = {
#     '2019-052001': {
#         '이름': '박찬호', '나이': 25, '성별': 'm', '연락처': '010-1234-5678', 
#         '이용서비스': ['헬스,수영']
#         , '할인율': 0},
#     '2019-052004': {'이름': '박용택', '나이': 65, '성별': 'm', '연락처': '010-9012-3456', 
#     '이용서비스': ['수영'], '할인율':50}}

# print(members['2019-052001']['이용서비스'])

#함수란, 특정 기능을 명시한 구문으로 기능을 재사용하기 위해서 사용합니다.
#vs변수란, 데이터를 관리하기 위한 메모리 공간으로 데이터를 재샤용하기 위해서 사용
'''
함수 기본 문법 구조
def 함수이름():
    기능(실행문)
'''
#함수를 정의(선언)했다.
def printIntro(): #--> 함수 선언부
    print('안녕하세요')
#함수는 호출(call)햇을 때 동작한다.
printIntro() #--> 함수 호출부

#함수는 기능을 최대한 작게 그리고 다른 프로그램에 이식하기 쉽게 만들자.
#계산기 프로그램을 함수를 이용해서 만들어보자.

def add():
    print(f'덧셈 결과: {num1 + num2}')
def sub():
    print(f'뺄셈 결과: {num1 - num2}')
def mul():
    print(f'곱셈 결과: {num1 * num2}')
def div():
    print(f'나눗셈 결과: {num1 / num2}')

def calculator():
    if operator == 1:
        add()
    elif operator == 2:
        sub()
    elif operator == 3:
        mul()
    elif operator == 4:
        div()



num1 = float(input('첫 번째 숫자 입력: '))
operator = int(input('연산자 입력: 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈'))
num2 = float(input('두 번째 숫자 입력: '))

calculator()

#유치원에 납품되는 계산기
def lowCalculator():
    if operator == 1:
        add()
    elif operator == 2:
        sub()

lowCalculator()