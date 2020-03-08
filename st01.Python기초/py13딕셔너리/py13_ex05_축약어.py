# 현대인들은 축약어를 많이 사용한다.  예를 들어서 "B4(Before)" "TX(Thanks)" 
# "BBL(Be Back Later)" "BCNU(Be Seeing You)" "HAND(Have A Nice Day)"와 
# 같은 축약어들이 있다. 축약어를 풀어서 일반적인 문장으로 변환하는 
# 프로그램을 작성하여 보자. 
# 
# 실행 예시)
# 번역할 문장을 입력하시오: TX Mr. Park!
# Thanks Mr.Park!

table = { 
        "B4": "Before",
        "TX": "Thanks",
        "BBL": "Be Back Later",
        "BCNU":"Be Seeing You",
        "HAND":"Have A Nice Day",
    }

# 작업 순서
# 1. 문자열 입력 받기
# 2. 문자열을 split() 해서 array 리스트로 만든다.
# 3. 반복문을 사용하여 array 리스트를 루프를 돌면서 
#    딕셔너리 table에서 찾는다.     
#     ==> table에서 찾을 때는 get()메서드나 in 연산자를 사용한다
# 3-1 찾았다면 바꾼다. replace()
# 4. 찾기 끝나면 출력한다.

# 1.
str = input("문자열을 입력하세요")

# 2. 문자열 나누기
array = str.split(" ")

for i in range( 0, len(array), 1 ) :
    print( array[i] ) # TX , Mr.  , Park! 

result = "" # 출력할 문자열
# 3. 반복문을 사용하여 array 리스트를 루프를 돌면서
for i in array:
    print(i) # TX , Mr.  , Park! 
    # 3-1 table에서 찾는다.
    # 찾을 때는 get()메서드나 in 연산자를 사용한다
    # 찾았다면 바꾼다. 
    # arry[0] = Tx    일때 table에서 찾으려면( get(), in )
    # arry[1] = Mr.   일때 table에서 찾으려면( get(), in )
    # arry[2] = Park! 일때 table에서 찾으려면( get(), in )
    value = table.get( i )
    if value == None :
        result = result + i  + " "
    else:        
        result = result + value + " " # value = array[i]
        
# 4. 출력한다 
print( result ) 




