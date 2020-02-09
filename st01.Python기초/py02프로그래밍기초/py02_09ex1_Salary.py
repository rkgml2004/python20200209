# py02_09ex1_Salary

# 변수 선언 : salary , deposit 변수(메모리 공간) 선언
salary = 0 # 이것은 정수다.
deposit = 0

# 숫자를 입력받고(이것은 문자열) salary 변수 에 저장하시오(넣으시오).
salary = input("월급을 입력하시오::") # 주의 사항. 이것은 문자다.

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.
print( type(salary) ) # <class, str>
deposit = 10 * 12 *  int(salary) # 10년치 월급의 총합
                                 # int(salary) 는 문자열을 정수로 바꾼다.

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.
print("10년 동안의 저축액:" ,  deposit, "원 입니다." )