# 데이터입력(input data)
#input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''

'''
print('정수를 입력하세요')
inputInteger = input()
print(inputInteger)
print(type(inputInteger))
'''

'''
print('실수 입력하세요.')
inputFloat = input()
print(inputFloat)
print(type(inputFloat))
'''

'''
print('논리형 데이터 입력하세요.', end='')
inputBoolean = input()
print(inputBoolean)
print(type(inputBoolean))
inputBoolean = input('논리형 데이터 입력하세요.')
'''

# userInputData = input('사용자야 정수 입력해라')
# print(userInputData)
# print(type(userInputData))
# userInputData = int(userInputData)
# print(type(userInputData))

# # str -> boolean
# userInputData = input('True or False 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = bool(userInputData)
# print(type(userInputData))

# str -> float
userInputData = input('실수 입력하세요.')
print(userInputData)
print(type(userInputData))
userInputData = float(userInputData)
print(type(userInputData))

userInputData = 'true'
userInputData = bool(userInputData)

x = 3
y = float(x)
print(y)

x=3.141592
y=int(x)
print(y)
print(float(y))