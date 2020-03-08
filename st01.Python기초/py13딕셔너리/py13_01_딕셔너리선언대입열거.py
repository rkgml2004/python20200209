
# 딕셔너리의 CRUD2S 사용법을 익힌다. 
# 딕셔너리에 담을 수 있는 것은? ==> 다
# 딕셔너리 선언 ==>  dic = { }
# 딕셔너리 추가(C) ==> dic["key값"] = "값"
# 딕셔너리 읽기(R) ==> dic["key값"]
# 딕셔너리 수정(U) ==> dic["key값"] = "값"
# 딕셔너리 삭제(D) ==> dic.pop("key값")
# 딕셔너리 정렬(S) ==> 없음. 왜냐하면 순서가 없기 때문
# 딕셔너리 검색(S) ==> 반복문 
# 딕셔너리 길이    ==> len(dic.keys() ) , len(dic.values() ) , 


# 딕셔너리 선언하기
dictionary = {
    "name" : "7D 망고",
    "type" : "당",
    "ingredient" :  ["망고", "설탕", "소금", "치자"],
    "origin" : "필리핀",
}

# 딕셔너리 전체 내용을 출력해봅니다.
print( dictionary ) # 전체 출력


# R: 요소 추가 전에 내용을 출력해봅니다.
# 1. 선택 연산자를 사용하는 방법
# 2. get() 메서드를 사용하는 방법
print( dictionary["name"]) # 요소 출력
print( dictionary["type"]) # 요소 출력
print( "head 값", dictionary.get("ingredient") ) # 요소 출력
print( "head 값", dictionary.get("origin") ) # 요소 출력


# C: 딕셔너리 추가
# dictionary의 key 에 head와 body 를 추가하고 값을 출력하시오 
dictionary["head"] = "머리"
dictionary["body"] = "몸"

print( "head 값", dictionary["head"] ) # 선택 연산자 [] 로 읽기 
print( "head 값", dictionary.get("head") ) # get() 메서드로 읽기 



# U: 딕셔너리 수정
# name 값을 "8D 망고" 로 수정하시오.
print( "name"  , dictionary["name"] )
dictionary["name"] = "8D 망고" # "7D 망고" --> "8D 망고" 변경
print( "name"  , dictionary["name"] )


# D: 딕셔너리 삭제.
# 1. 연산자 방식 ==> del . 비추천
# 2. 메서드 방식 ==> .pop("key"). 추천
# name, type 키를 삭제
print( "딕셔너리 삭제 전", dictionary)
dictionary.pop("name")
dictionary.pop("type") 
print( "딕셔너리 삭제 후", dictionary)

# S: 정렬. 딕셔너리는 정렬하는 방법이 없다. 
# 단, key 값만 정렬하는 것은 가능하다, value 값만 정렬하는 것은 가능하다.


# S: 검색. 특별하는 방법이 없다.  
# 선택연산자를 사용하면 바로 검색 되기 때문




# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# try ~ except 를 추가하시오.  
try:
    dictionary["존재하지 않는 키"] # KeyError
except KeyError as ex:
    print( ex ) # 화면에 에러 출력하고 다름 라인 실행. 
	
	
# 존재하지 않는 키에 접근하면 에러 발생. try ~ except 를 추가하시오.  
# 딕셔너리에서 키의 존재 여부 확인.  
# 방법1. get() 메서드 사용하는 방법
#        get() 메서드 키가 존재하지 않는 경우에  None을 반환한다. 
# 방법2. in 연산자를 사용하는 방법

# 방법1. get() 메서드 사용하는 방법
value = dictionary.get("존재하지 않는 키") # vaule 값이 None 이면 키가 없다는 의미다.
if value == None :
    print("키가 존재하지 않는다")
else:
    print("키값이 존재한다")
    print( value )

# 방법2. in 연산자를 사용하는 방법
if "존재하지 않는 키" in dictionary:
    print("키값이 존재한다")    
    print(dictionary["존재하지 않는 키"])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

print()


###################
# 딕셔너리 열거
# key 만 열거. keys() 메서드 사용.
# value 만 열거. values() 메서드 사용.
# key 와 value를 쌍으로 열거. items() 메서드 사용.
##################

# key 만 열거. keys() 메서드 사용.
for key in dictionary.keys():
    print("keys >>> ", key)
print()

# value 만 열거. values() 메서드 사용.
for value in dictionary.values():
    print("values >>> ", value)
print()

# key, value를 쌍으로 열거. items() 메서드 사용.
for item in dictionary.items():
    print("items >>> ", item[0], item[1] )
print()
