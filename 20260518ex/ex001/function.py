#함수 정의
'''
사용자 함수를 만든다는 것을 함수를 정의한다 라고 한다.
함수를 정의할 때 def 키워드를 사용합니다. 그리고 함수명 콜론(:), 실행부를 이용합니다.
'''
'''
def 함수명():
    실행부(함수 기능)
'''

def greet():
    print('안녕하세요.')
    print('반갑습니다.')
    print('저는 홍길동입니다.')

'''
함수명 규칙
1. 내장함수명과 동일하면 안된다.
2. 첫 글자는 주로 소문자로시작한다.
3. 첫 글자는 숫자로 시작할 수 없다.
4. 특수문자는 사용할 수 없지만 언더바는 사용가능
5. 두 개 이상의 단어가 조합되는 경우 스네이크 또는 카멜표기법을 사용하자.
'''

#온도센서 작동 시스템 만들기
#온도센서 작동을 시작하고 멈추는 함수를정의

#함수 선언부
def strtTemperatureSensor():
    print('온도센서 작동을 시작합니다.')

def stopTemperatureSensor():
    print('온도센서 작동을 중지합니다.')

#함수 호출
strtTemperatureSensor()
stopTemperatureSensor()

#내 노트북은 몇 인치일까?
'''
노트북 사이즈에 맞는 파우치를 하나 구매하려는데 사이즈 표에 인치로만 표시되 있다.
cm를 인치로 바꿔주는 함수를 만들자
1inch = 0.393701cm 
'''
# def convertUnit():
#     lengthCM =float(input('길이(cm) 입력:'))
#     print(f'{lengthCM * 0.393701}inch')

# convertUnit()
# convertUnit()
# convertUnit()

#이동 거리를 계산하는 함수
'''
길동이는 5시간 동안 3km/h의 속도로 등산을 했습니다.
등산한 시간과 속도를 입력하면 이동한 거리를 걔산해주는 프로그램을 함수를 이용하여 만들기
'''
# def calculateDistance():
#     print(f'이동거리: {hourData * speedData}km')

# hourData = float(input('이동 시간: '))
# speedData = float(input('이동 속도: '))

# calculateDistance()

# #pass
# def calculateNumber():
#     pass

#함수 내에서 또 다른 함수 호출

def fun1():
    print('fun1() CALLED!!')
def fun2():
    print('fun2() CALLED!!')

def fun3():
    fun1()
    fun2()
    print('fun3() CALLED!!')    

fun3()
'''
print('fun1() CALLED!!')
print('fun2() CALLED!!')
print('fun3() CALLED!!') 
'''
# def fun4():
#     print('fun4() CALLED!!') 
#     fun4()

# fun4()

#다국어 인사말 프로그램 by 함수
'''
출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램을 
함수를 이용해 만들기
1.한국    2.USA    3.Japan
'''
# def introKor():
#     print('안녕')

# def introEng():
#     print('hello')

# def introJap():
#     print('12155')

# selectedMenuNUM = int(input('where are you from? 1.한국    2.USA    3.Japan'))

# if selectedMenuNUM == 1:
#     introKor()
# elif selectedMenuNUM == 2:
#     introEng()
# elif selectedMenuNUM == 3:
#     introJap()

#계산기 프로그램
'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램
'''
def calculator():
    if selectedOperator == 1:
        print(f'덧셈결과: {inputNumber1 + inputNumber2}')
    elif selectedOperator == 2:
        print(f'뺄셈결과: {inputNumber1 - inputNumber2}')
    elif selectedOperator == 3:
        print(f'곱셈결과: {inputNumber1 * inputNumber2}')
    elif selectedOperator == 4:
        print(f'나눗셈결과: {inputNumber1 / inputNumber2}')


inputNumber1 = float(input('숫자를 입력하세요.'))
selectedOperator = int(input('연산자를 선택하세요. 1.덧셈  2.뺄셈  3.곱셈  4.나눗셈'))
inputNumber2 = float(input('숫자를 입력하세요.'))

calculator()


