
# 내장함수
value = abs(-100)
print(value)


# 사용자함수


def add1(a,  b):  # 반환값이 있는 경우 : 반환값의 타입 사용
    result = a + b
    return result  # 반환값의 타입과 함수 리턴 타입이 동일


def add2(x):    # 반환값이 없는 경우 : void 타입 사용
    print(x)
    return


result = add1(1, 3)
print(result)

add2(result)
