#################################
# os 모듈의 사용법을 익힌다.
#
# os.path.isfile() 메서드는 있으면 True 없으면 False 를 반환한다.
#################################


# os 모듈을 읽어 들입니다.
import os 


#######################
# 파일 존재 유무 체크. 
# os.path.isfile() 을 사용하여 파일의 존재 여부를 확인 할 수 있다. 
# os.path.isfile() 메서는 있으면 True 없으면 False 를 반환한다.
# 1. 상대 경로를 사용하는 경우 
#    ../ 부모 폴더
#    ./  현재 폴더 
# 2. 절대 경로를 사용하는 경우 
#   C:\Intel\aa.txt
#   D:\Intel\aa.txt
# 
# 현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
# os.path.isfile() 메서드는 있으면 True 없으면 False 를 반환한다.
print( "현재 작업 디렉토리: ", os.getcwd() )
if os.path.isfile("./st01.Python기초/py23표준모듈/phones.txt") :
    print("파일 존재")
else :
    print("파일 없음")


#######################
# 현재 폴더의 파일/폴더를 출력합니다.
output = os.listdir(".")
print("os.listdir():", output)
print()


#######################
# 현재 폴더의 파일/폴더를 구분합니다.
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)


#######################
# 폴더를 읽어 들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
        else:
            # 파일이라면 출력하기
            print("파일:", item)


# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")




