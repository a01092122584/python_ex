#CRUD
'''
c: create 생성, 추가
r: read   조회
u: update 수정 
d: delete 삭제
'''

'''
딕셔너리(dictionary): {key: value}
'''
#c: create 생성, 추가
student = {'학번': 123456789, '이름': '홍길동', '나이': 20, '성별': 'm',
            '연락처': '010-1234-5678'}
print(f'student: {student}')
print(f'student type: {type(student)}')

#r: read   조회
sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')

#u: update 수정
sName = student['이름']
print(f'sName: {sName}') # 홍길동 > 홍길자

student['이름'] = '홍길자'
sName = student['이름']
print(f'sName: {sName}')

#d: delete 삭제
del student['연락처']
print(f'student: {student}')

#keys(), values(), items()
#keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다. 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')
for key in keys:
    print(f'key: value = {key}: {student[key]}')

#values(): 딕셔너리에서 벨류값들만 몽땅 뽑는다. 뽑은 벨류들은 리스트와 비슷한 데이터 타입.
values = student.values()
print(f'values: {values}')
print(f'values type: {type(values)}')
for value in values:
    print(f'value: {value}')

items = student.items() #key & value
print(f'items: {items}')
for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0], item[1]}')
for key, value in items:
    print(f'key: value = {key}: {value}') #구조분해할당 문법

#구조분해할당
# a, b =(10, 20)
# print(f'a: {a}, b: {b}')

# c = (10, 20)
# a = c[0]
# b = c[1]
# print(f'a: {a}, b: {b}')

# a = 10
# b = 20

# #swapping a: 20, b: 10
# # temp = a
# # a = b     # a = 20
# # b = temp  # b = 10
# a, b = b, a
# print(f'a: {a}, b: {b}')

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''

# a, b, *c = scores
# print(f'a: {a}')
# print(f'b: {b}')
# print(f'c: {c}')

members ={'2019-052001': '박찬호+25+m+010-1234-5678+헬스,수영+0'}
info = members['2019-052001']
print(f'info: {info}')

infos = info.split('+')
print(f'infos: {infos}')
