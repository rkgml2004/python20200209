# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"

#################################
# 문자열 연산자
#################################

# 문자열 결합 연산자 : +
# "A barking Dog never Bites!"를 출력하시오.
bite = " never Bites!"
str = prov + bite 
print( str ) # "A barking Dog never Bites!"

# 문자열 반복 연산자 : *

# 문자열 일치 연산자 : ==
# s09 = "abcde"; s10 = "abcde" 일 때
# s09 과 s10 이 같으면 "same"을 아니면 "not same"을 출력하시오


# 문자열 슬라이싱 연산자 : []
# 문자열 자체가 리스트 취급을 당하기 때문에 그냥 리스트에서 특정 구문을 빼오듯이 쓰면 된다.
# (2번째부터 4번째 자리까지 추출:  bar)
bar = prov[2:5]
print(bar ) # bar

# prov 에서 Dog 전까지만 출력하시오. Dog를 앞에서 부터 검색
idx = prov.find("Dog")
if idx != -1:
    dog = prov[idx:idx+3]
    print(dog) # Dog


# 문자열 추출:
# "A barking dog"에서 마지막 g 빼고 "A barking Do" 를 출력하시오. g를 뒤 부터 검색.

# 첫번째 b 문자의 위치를 출력하시오.
