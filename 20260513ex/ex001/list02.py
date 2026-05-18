#리스트 정렬
'''
sort 함수는 리스트의 아이템을 정렬하는 데 사용합니다.
reverse 옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬합니다.
'''
numbers = [5, 1, 3, 4, 6]
print(f'numbers: {numbers}')      #[5, 1, 3, 4, 6]

#오름차순(ASC) ()안채워도됨
numbers.sort(reverse=False)
print(f'numbers: {numbers}')      #[1, 3, 4, 5, 6]

#True면 내림차순(DESC)
numbers.sort(reverse=True)
print(f'numbers: {numbers}')      #[6, 5, 4, 3, 1]

korean = ['다', '가', '마', '하', '카']
print(f'korean: {korean}')

korean.sort()
print(f'korean: {korean}')

korean.sort(reverse=True)
print(f'korean: {korean}')

scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
print(f'scores: {scores}')
scores.sort()
print(f'scores: {scores}')
scores.sort(reverse=True)
print(f'scores: {scores}')

# quiz) 회의 참석자 정렬하기
# 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
names.sort()
print(f'names: {names}')

names.sort(reverse=True)
print(f'names: {names}')

#리스트 순서 뒤집기
#reverse 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있습니다.
vegetables = ['당근', '오이', '양파', '감자', '고구마']
vegetables.reverse()
print(f'vegetables: {vegetables}')

#리스트 슬라이싱
#슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것을 말합니다.
animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(f'animals: {animals}')
print(f'animals[1:4]: {animals[1:4]}')

sliceAnimals = animals[1:4]
print(f'sliceAnimals: {sliceAnimals}')
#[n:m] : n  인덱스부터 (m-1) 인덱스 까지에 아이템을 슬라이싱(추출)한다.

animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(f'{animals[:3]}') #인덱스 0부터 2(3-1)까지 슬라이싱

print(f'{animals[3:]}') #인덱스 3부터 끝까지 슬라이싱
 
#뒤에서 2개의 아이템을 슬라이싱
print(f'{animals[len(animals)-2]}')

print(f'{animals[:-1]}') #뒤에서 하나빼고
print(f'{animals[1:-1]}')

print(f'{animals[:]}') #전체데이터

print(f'{animals[::2]}')#스텝 2칸씩 건너뜀

#다음 리스트를 보고 답하시오.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 1 alphabet 역순으로 출력
alphabet.reverse()
print(f'alphabet: {alphabet}')

# #2  다음 요구사항에 맞게 alphabet 리스트를 슬라이싱하시오
'''
 - 인덱스 2부터 5까지의 아이템을 출력하시오.
 - 인덱스 0부터 4까지의 아이템을 출력하시오.
 - 인덱스 3부터 7까지의 아이템을 출력하시오.
 - 인덱스 5부터 끝까지의 아이템을 출력하시오.
 - 인덱스 3부터 8까지의 아이템을 출력하시오.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f'{alphabet[2:6]}')
print(f'{alphabet[:5]}')
print(f'{alphabet[3:8]}')
print(f'{alphabet[5:]}')
print(f'{alphabet[3:9]}')

#뒤에서 4개 아이템을 출력하시오.
print(f'{alphabet[len(alphabet)-4:]}')
print(f'{alphabet[-4:]}')

#1숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#[3, 7, 1, 9, 5]
nums = [3, 7, 1, 9, 5]

nums.sort(reverse=True)

maxNum = nums[0]

print(f'가장 큰 숫자: {maxNum}')
# print(max(nums))

#2사용자에게 숫자 입력받아서 1부터 입력한 숫자까지 합계 출력

userInputNum = int(input('양수 입력하세요'))
total = 0
for num in range(1, userInputNum+1):
    total += num

print(f'total: {total}')

#3 리스트에 있는 숫자 중 짝수만 출력하기 [1,2,3,4,5,6]

nums = [1,2,3,4,5,6]
for num in nums:
    if num % 2 == 0:
        print(f'num: {num}')

#4 리스트 숫자를 오름차순 정렬하기 [5,1,7,3]
nums = [5,1,7,3]

nums.sort()

print(f'nums: {nums}')

#5 리스트 숫자를 내림차순 정렬하기 [5,1,7,3]
nums = [5,1,7,3]

nums.sort(reverse=True)

print(f'nums: {nums}')

#6 리스트 숫자 평균 구하기 [10,20,30]
nums = [10,20,30]
total = 0
average = 0

for num in nums:
    total += num
average = total / len(nums)
print(f'total: {total}')
print(f'average: {average}')

#7. 리스트에서 가장 작은 숫자 찾기 (min() 사용 금지)

#8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

#9. 사용자가 입력한 숫자를 리스트에 저장하다가 0 입력하면 종료 후 리스트 출력하기[입력: 3 ,입력: 7, 입력: 2 ,입력: 0]