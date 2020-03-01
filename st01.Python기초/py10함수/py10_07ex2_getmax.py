# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자. 

# 함수 정의
# x : 매개변수
# y : 매개변수

def getmax( x, y) :
    result = None # None : 값이 없다.

    if x > y:
        result = x # x 반환 
    else:
        result = y# y 반환

    return result

def myinput( mesg ) :
    try:
        n1 = input( mesg )
        n1 = int( n1 )
    except ValueError as ex:
        print( ex )

    return n1

# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다 
def main():
    # 입력 처리
    n1 = myinput( "첫번째 정수 입력: " )
    n2 = myinput( "두번째 정수 입력: " )

    # 최대 값 출력
    val = getmax( n1, n2)
    print( val )

main()