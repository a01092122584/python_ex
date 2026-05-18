# flag = True

# members = {}

# while True:
#     selectedMenuNum = int(input('1.회원가입   2.프로그램 종료'))

#     if selectedMenuNum == 1:
#         id = input('아이디: ')
#         pw = input('비밀번호: ')
#         members[id] = pw

#     elif selectedMenuNum == 2:
#         flag = False

#         for key in members.keys():
#             print(f'ID: {key}, PW: {members[key]}')1


'''
classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 'Java':'5학점', 'Javascript':'3학점'}

classes['HTML5'] = '5학점'
classes['Javascript'] = '5학점'
print(f'classes: {classes}')



members = {'2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스,수영', 0],
           '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
           '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]}
#전체 회원 정보 출력

for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

#전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별만 출력

for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')
'''

members = {'2019-052001': {'이름':'박찬호', '나이': 25, '성별': 'M', '연락처': '010-1234-5678', '이용서비스': ['헬스', '수영'], '할인율': 0},
           '2019-052004': {'이름':'박용택', '나이': 65, '성별': 'M', '연락처': '010-9012-3456', '이용서비스': ['수영'], '할인율': 50},
           '2019-052003': {'이름':'박세리', '나이': 70, '성별': 'W', '연락처': '010-7890-1234', '이용서비스': ['아쿠아로빅'], '할인율': 50}}

#전체 회원 정보 출력
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

#이름,성별,이용서비스 그리고 이용서비스 개수 출력
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')


vegetables = {'당근' : 0, '건대추': 0, '대파': 0, '애호박': 0, '부추': 0}
vegetables['당근'] += 10
vegetables['건대추'] += 100
vegetables['대파'] += 20
vegetables['애호박'] += 3
vegetables['부추'] += 1


vegetables['당근'] -= 1
vegetables['건대추'] -= 10
vegetables['대파'] -= 1
vegetables['애호박'] -= 1
vegetables['부추'] -= 1


for name, count in vegetables.items():
    print(f'{name}: {count}개')





