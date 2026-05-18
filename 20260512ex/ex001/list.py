#컨테이너 자료형 > 자료형 (container data type)

'''
컨테이너 자료형으로는 리스트 (list),튜플 (tuple),딕셔너리 (dictionary)이 있다.
'''
#list: 정의(선언 + 초기화)
#인덱스(index): 아이템에 부여된 아이템 식별 
#리스트의 길이 len 함수
#리스트의 전체 데이터 조회
#리스트는 반복 가능한 객체(데이터)이다. 이터러블한 데이터

# 대괄호를 이용해서 데이터를 묶고 데이터와 데이터는 쉼표로 구분.
#같은 유형의 데이터를 나열 데이터의 갯수를 길이라고 함.
#변수에 리스트 자체가 아닌 데이터 첫 번째 메모리 주소가 담김

# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나'] 
# print(f'fruits: {fruits}')
# print(f'type of fruits: {type(fruits)}')

'''
리스트에 포함되는 데이터는 어떤 자료형이든 상과없음
예를 들어 정수, 실수, 문자(열)이 하나의 리스트로 묶일 수도 있습니다.
'''
complexList = [10, 3.14, 'a', 'hello']
#이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을수 있는 언어는
#파이썬과 javascript뿐이다. java는 안된다.
print(f'complexList: {complexList}')
print(f'type of complexList: {type(complexList)}')

member = []
print(f'member: {member}')
print(f'type of member: {type(member)}')

#다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자
attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']

#how to 리스트의 아이템 조회
#특정 아이템 조회
#index는 아이템마다 자동으로 부여되는 일종의 번호표로 항상 0부터 시작합니다.
#           0       1      2      3     4      5       6        7
fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나'] 
print(f'fruits[1]: {fruits[1]}')
print(f'fruits[0]: {fruits[0]}')
print(f'fruits[7]: {fruits[7]}')
#만약 리스트에서 존재하지 않는 인덱스를 참조하면 어떻게 될까요 > indexError 발생

#리스트 길이(아이템 개수) 조회
'''
리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len 함수를 사용하면 알 수 있습니다.
다음은 len 함수를 이용해서 리스트의 길이를 확인하는 코드입니다.
리스트의 마지막 아이템의 인덱스 값은 '리스트의 길이 - 1' 이다.
'''
numbers = [1, 2, 3, 4, 5]
print(f'numbers: {numbers}')
print(f'numbers length: {len(numbers)}')

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 99]
#첫 번째 데이터 조회:
print(f'첫 번째 데이터: {numbers[0]}')

#마지막 데이터 조회:
print(f'마지막 데이터: {numbers[len(numbers)-1]}')

#len 함수는 문자열의 길이를 조회하는데에도 사용된다.
str = 'helll   lllll    lo'
print(len(str))

#입력한 글자 수 확인하기
'''
사용자로붙터 메시지를 받고 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어봅시다.
'''

#msg = input('메시지 입력: ')
#msgLen = len(msg)
#print(f'msgLen: {msgLen}')

#리스트 전체 데이터 조회
#balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
#print(f'balls[0]')
#print(f'balls[1]')
#print(f'balls[2]')
#print(f'balls[3]')
#print(f'balls[4]')

#for 변수 in enemerate(balls) 
# for fruit in fruits
#print(f'fruit: {fruit}')
#인덱스, 아이템 값 구하는법
# 1.for idx, fruit in enumerate(fruits):
# 2.print(f'index: {idx}, fruit: {fruit}')

#idx = 0
#for idx, item in enumerate(balls):
 #   print(f'item: {item}, index: {idx}')

balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
i = 0
while i < len(balls):
    print(f'{balls[i]}, index: {i}')
    i += 1

#다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오
sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
lenVar = len(sports) - 1
print(sports[lenVar])

#다음 리스트에서 python 문자열의 인덱스 값을 출력하는 프로그램을 만드시오
languages = ['C/C++', 'C#', 'python', 'jave']
for idx, str in enumerate(languages):
    if str == 'python':
        print(f'python idx: {idx}')

targetIdx = languages.index('python')
print(f'targetIdx: {targetIdx}')

#아이템 기존 리스트에 삽입
#리스트 마지막에 삽입
# sports = ['football', 'baseball','volleyball']
# print(f'sports: {sports}')

# sports.append('basketball')
# print(f'sports: {sports}')
# print(f'sports lenght: {len(sports)}')

'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가 되는 프로그램을 만들어보자
취미의 개수를 출력
'''
hobbies =   []
flag = True
'''
while True:
    hobby = input('취미 입력:')
    hobbies.append(hobby)
    print(f'hobbies: {hobbies}')
    selectedMenuNumber = int(input('1.취미 추가 2.종료'))
    if selectedMenuNumber == 2:
        break
'''    

#특정 위치에 아이템 삽입 
#리스트의 원하는 위치에 아이템을 삽입할 때는 insert 함수를 이용합니다.
#마지막 위치에 삽입 append
# countries = ['korea', 'china', 'japan']
# countries.insert(1, 'usa')
# print(f'countries: {countries}')

#누락된 숫자 추가하기
#numbers = [1, 2, 3, 4, 5, 7, 8, 9] 1~10까지 누락된 숫자를 추가해보자.
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6)
# print(f'numbers: {numbers}')
# numbers.append(10)
# print(f'numbers: {numbers}')

#리스트 연결하기
#리스트에 또 다른 리스트를 연결할 때는 extend 함수를 사용
# list1 = [1, 2, 3]
# print(f'list1: {list1}')
# list2 = [10, 20, 30]
# print(f'list2: {list2}')

# list1.extend(list2)
# print(f'list1: {list1}')

#list3 = list1 + list2 새로운 메모리 공간에 만들어진다.
#print(f'list1: {list1}')
#print(f'list2: {list2}')
#print(f'list3: {list3}')

# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제 pop

# sports = ['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports: {sports}')
# sports.pop()
# print(f'sports: {sports}')
# sports.pop(1)
# print(f'sports: {sports}')

removedItem = sports.pop()
print(f'removedItem: {removedItem}')
#특정 위치 아이템 삭제 pop에 index값을 넣기 []
#pop()대신 del 키워드를 이용해서 아이템을 삭제할 수 있다.
sports = ['football', 'baseball', 'volleyball', 'basketball']
del sports[2]
print(f'sports: {sports}')

#pop vs del
nums =[1, 2, 3, 4, 5, 6]
deletedNum = nums.pop(3) 
print(f'deletedNum: {deletedNum}')

#특정 아이템 삭제 by 아이템
languages= ['C/C++', 'C#', 'java', 'python']
#languages.pop(2) #['C/C++', 'C#', 'python']
languages.remove('java') #['C/C++', 'C#', 'python']
print(f'languages: {languages}')

#remove()를 이용해서 아이템을 삭제할 떄 삭제하려는 아이템의 개수가 2개 이상일 때 처음 아이템만 삭제됨
languages = ['C/C++', 'C#', 'java', 'python', 'java']
languages.remove('java')
print(f'languages: {languages}')

# 과일 리스트에서 야채를 찾아 삭제하기
'''
['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
당근과 토마토를 찾아 삭제하는 프로그램
'''

fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print(f'fruits: {fruits}')

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)
print(f'fruits: {fruits}')

#합격 여부 판정하기
'''
다음은 홍길동 수험생의 2020년 공인중개사 자격증 시험 성적표입니다.
아래 합격 기준에 만족하는지 구하는 프로그램을 만들어봅시다.
 - 매 과목 100점을 만점으로 하여 매 과목 40점 이상
 - 전 과목 평균 60점 이상 득점
홍길동 수험생 성적표
부동산 개론: 55
민법: 35
공법: 40
공시법: 70
세법: 65
중개사법: 30
'''

scores = [55, 35, 40, 70, 65, 30]
total        = 0      #총점
underSubject = 0      #과락 과목 개수
average      = 0 

for score in scores:
    if score < 40:    #과락 과목 개수
        underSubject += 1 
    
    total += score    #총합
print(f'40점 미만 과목 수: {underSubject}')
average = total/ len(scores)

print(f'평균: {average:.2f}')       #지향하자
#print(f'평균: {total / 6}')                     지양하자

#합격 여부
if underSubject > 0 or average < 60:
    print(f'아쉽습니다. 다음 기회에')
else:
    print(f'축 합격')

#sports 리스트에서 'volleyball' 을 삭제하는 프로그램을 만들자.
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# volleyballIdx = sports.index('volleyball')
# sports.pop(volleyballIdx)
# print(f'sports: {sports}')