# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle


############################
# 리스트 선언
# 리스트에는 다 담을 수 있다. 함수도 담을 수 있다. 
array = []
array = list() 
array = [1, 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None ]

############################
# 문자 H, e, l, l, o를 요소로 가지는 리스트
# 문자열 Hello를 요소로 가지는 리스트
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
list1 = [ "H", "e", "l", "l", "o"]
print( type(list1), list1) # <class 'list'>  ["H", "e", "l", "l", "o"]

list2 = ["Hello"]
print( type(list2), list2)  # <class 'list'>  ["Hello"]

list4 = list( "Hello" )
print( type(list4), list4)  # <class 'list'>  ["H", "e", "l", "l", "o"]

list3 = [0,1,2,3,4]
print( type(list3), list3)  # <class 'list'>  [0,1,2,3,4]

list5 = list( range(0,5,1) )
print( type(list5), list5)  # <class 'list'>  [0,1,2,3,4]



############################
# 리스트 요소 출력
# 리스트의 시작은 0번부터다. 
# 리스트  Read : [] 선택 연산자를 사용한다.
############################
array = [1, 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None ]
print( "array[0]", type(array[0] ), array[0] ) 
print( "array[4]", type(array[4] ), array[4] ) 
print( "array[5]", type(array[5] ), array[5] ) 
print( "array[6]", type(array[6] ), array[6] ) 

############################
# 리스트 전체 출력
############################
print( "array", array ) 

############################
# 리스트 슬라이싱 : 
# 1. 선택 연산자 사용하는 방법.
############################
array = [1, 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None ]
print( "array[0]   ", array[0]  ) # 1
print( "array[1:3] ", array[1:3]) # [1.1, "문자"] 
print( "array[-1]  ", array[-1] ) # None
print( "array[-3]  ", array[-3] ) # [0,1]


############################
# 리스트 요소 대입
# 리스트의 0번 값을 문자열 "변경"값으로 바꾸시오.
############################
print( "array[0]   ", array[0]  ) # 1
array[0] = "변경"
print( "array[0]   ", array[0]  ) # 변경


############################
# 리스트 요소 추가: C. create
#  추가 : 리스트의 마지막에 넣는다. --> .append() 메서드 사용
#  삽입 : 리스트의 중간에 넣는다.   --> .insert() 메서드 사용
############################ 
print( "array", array ) # ["변경", 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None ]
array.append( "추가")
print( "array", array ) # ["변경", 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]
array.insert(0, "삽입") 
print( "array", array ) # ["삽입", "변경", 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]


############################
# 리스트 요소 삭제: D. deletef
#  메서드 방식 --> pop() 메서드 . 추천
#  연산자 방식 --> del. 비추천 
############################
print( "array", array ) # ["삽입", "변경", 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]
array.pop(0) # 메서드 방식의 삭제
print( "array", array ) # ["변경", 1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]
del array[0] 
print( "array", array ) # [1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]

############################
# 리스트 열거
############################
print( "array", array ) # [1.1, "문자", True, [0,1] , {"a": 1, "1": "ba"}, None, "추가" ]
for i in array:
    print("리스트 열거 ", i)


############################
# 리스트에 담을 수 있는 것은? ==> 다
# 리스트 선언 ==> [] , list()
# 리스트 추가(C) ==> .append(), .insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> .pop()
# 리스트 정렬(S) ==> sorted()
# 리스트 정렬(S) ==> .find() + 반복문 , .rfind() + 반복문 
# 리스트 길이    ==> len()
# 리스트 출력 
# 리스트 열거
############################
