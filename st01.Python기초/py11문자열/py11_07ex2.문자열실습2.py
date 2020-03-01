# 문자열에서 가장 큰 수를 찾으시오.
# ※ 프로그램의 시작점은 main() 메서드가 되도록 만든다.
# ※ 프로그램을 최대한 작은 조각으로 분리하여 작성한다.
# 
# 문자열로 본다면 가장 큰 수는 9883 이지만
# 정수로 본다면 가장 큰 수는 73646 이다. 
# 
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다. 
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.        
# temp3 = "74 874 9883 73 9 73646 774"

def main():
    temp3 = "74 874 9883 73 9 73646 774"

    # a. 문자열 자르기 --> 리스트를 얻게 됨.
    lst = temp3.split(" ") # ["74","874","9883","73","9","73646","774"]
    print( type(lst), lst ) # 문자열 리스트 

    # lst의 값을 출력 
    # lst의 방번호는 0번 부터 시작한다
    print( lst[0] ,type( lst[0] ) ) # "74" <class 'str'>
    print( lst[1] ,type( lst[1] ) ) # "874" <class 'str'>
    print( lst[2] ,type( lst[2] ) ) # "9883" <class 'str'>
    print( max( lst) ) # 9883

    # b. 문자열을 정수 리스트로 만든다. 
    lst[0] = int( lst[0] ) # 
    lst[1] = int( lst[1] ) # 
    lst[2] = int( lst[2] ) # 
    print( lst[0] ,type( lst[0] ) ) # 74 <class 'int'>
    print( lst[1] ,type( lst[1] ) ) # 874 <class 'int'>
    print( lst[2] ,type( lst[2] ) ) # 9883 <class 'int'>

    for i in range(0, len(lst), 1 ):
        lst[i] = int( lst[i] ) # 
    print( type(lst), lst ) # 정수 리스트. [74,874,9883,73,9,73646,774]

    # c. 정수리스트를 오름차순 정렬하시오
    lst = sorted( lst ) # [9,73,74,774,874,9883,73646]

    # d. 정수리스트에서 최대값을 찾는다. 
    print( len(lst) )
    print( lst[ len(lst) - 1 ] ) # 73646. 마지막방에 있는 값. len(lst) - 1 == 6
    print( max( lst) ) # 73646

if __name__ == "__main__" :
    main() 
