# 왜 반복을 사용하나?


# 순차문
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")

# for 문
for x in range(5): #range(5) : 0부터 5전까지 1씩 
    print(x, "환영합니다")

for x in range(0,5,1): #range(5) : 0부터 5전까지 1씩 
    print(x, "환영합니다")


# while 문
i = 0
while i < 5:
    print('환영합니다.')
    i = i + 1
print('반복이 종료되었습니다.')
