# goods = {
#     '새우깡': 1200,
#     '비비빅': 400,
#     '초코파이': 500,
#     '맛동산': 1500
# }

# totalPrice = 0

# def shrimpCrackerPrice():
#     global totalPrice
#     totalPrice += goods['새우깡'] * shrimpCrackers
#     print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}원')

# def bibibigPrice():
#     global totalPrice
#     totalPrice += goods['비비빅'] * bibibigs
#     print(f'비비빅 구매 금액: {goods['비비빅'] * bibibigs}원')

# def chocopiPrice():
#     global totalPrice
#     totalPrice += goods['초코파이'] * chocopis
#     print(f'초코파이 구매 금액: {goods['초코파이'] * chocopis}원')

# def matdongsanPrice():
#     global totalPrice
#     totalPrice += goods['맛동산'] * matdongsans
#     print(f'맛동산 구매 금액: {goods['맛동산'] * matdongsans}원')

# shrimpCrackers = int(input('새우깡 구매 개수: '))
# bibibigs = int(input('비비빅 구매 개수: '))
# chocopis = int(input('초코파이 구매 개수: '))
# matdongsans = int(input('맛동산 구매 개수: '))

# print(f'새우깡 구매 개수: {shrimpCrackers}')
# print(f'비비빅 구매 개수: {bibibigs}')
# print(f'초코파이 구매 개수: {chocopis}')
# print(f'맛동산 구매 개수: {matdongsans}')
# print('=' * 40)
# shrimpCrackerPrice()
# bibibigPrice()
# chocopiPrice()
# matdongsanPrice()
# print('=' * 40)
# print(f'총 구매 금액: {totalPrice}')
# print('=' * 40)

# totalPrice = 0
# items = {
#     '우유': 2500,
#     '빵': 1500,
#     '계란': 6000
# }

# def milkPrice():
#     global totalPrice
#     totalPrice += items['우유'] * milkCount
#     print(f"우유구매금액: {items['우유'] * milkCount}원")

# def breadPrice():
#     global totalPrice
#     totalPrice += items['빵'] * breadCount
#     print(f"빵구매금액: {items['빵'] * breadCount}원")

# def eggPrice():
#     global totalPrice
#     totalPrice += items['계란'] * eggCount
#     print(f"계란구매금액: {items['계란'] * eggCount}원")


# milkCount = int(input('우유 구매 개수'))
# breadCount = int(input('빵 구매 개수'))
# eggCount = int(input('계란 구매 개수'))

# print('=' * 30)

# milkPrice()
# breadPrice()
# eggPrice()

# print('=' * 30)
# print(f'총 구매 금액: {totalPrice}원')
totalPrice = 0
menus = {
     '아메리카노': 3000,
     '라떼': 4000,
     '케이크': 4500
}

def americanoPrice():
    global totalPrice
    totalPrice += menus['아메리카노'] * americanoCount
    print("아메리카노 구매 금액: {menus['아메리카노'] * americanoCount}원")
def lattePrice():
    global totalPrice += menus['라떼'] * int(input('라떼 구매 개수'))
    print("라떼 구매 금액: {menus['아메리카노'] * americanoCount}원")
def cakePrice():
    global totalPrice += menus['케이크'] * int(input('케이크 구매 개수'))
    print("아메리카노 구매 금액: {menus['아메리카노'] * americanoCount}원")
int(input('아메리카노 구매 개수'))