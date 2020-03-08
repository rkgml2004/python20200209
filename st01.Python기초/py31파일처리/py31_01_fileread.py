import os

# 파일 존재 여부 확인
# 현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
# os.path.isfile() 메서는 있으면 True 없으면 False 를 반환한다.
print( "현재 작업 디렉토리: ", os.getcwd() )
if os.path.isfile("./st01.Python기초/py31파일처리/file/phones.txt") :
    print("파일 존재")
else :
    print("파일 없음")

#########################
# readline() 파일에서 한 줄씩 읽기
print("readline() 파일에서 한 줄씩 읽기")

# 읽기 모드로 파일 열기, 이 때 encoding 을 지정한다.
pfr = open("./st01.Python기초/py31파일처리/file/phones.txt", "r", encoding="UTF-8") 

s = pfr.readline() # 한 줄 읽기
print(s, end="") # 모니터에 출력
s = pfr.readline() # 한 줄 읽기
print(s, end="") # 모니터에 출력
s = pfr.readline() # 한 줄 읽기
print(s, end="") # 모니터에 출력

# 파일 닫기
pfr.close()

print()


#########################
## 반복문으로 파일에서 읽어서 모니터에 출력하기 
print("반복문으로 파일에서 읽어서 모니터에 출력하기")
# 읽기 모드로 파일 열기, 이 때 encoding 을 지정한다.
pfr = open("./st01.Python기초/py31파일처리/file/phones.txt", "r", encoding="UTF-8") 

line = pfr.readline()
while line != "":
    # 모니터에 출력
    print(s, end="") # 모니터에 출력

    # 다시 파일에서 읽기
    line = pfr.readline() # 한 줄 읽기

# 파일 닫기
pfr.close()


#########################
##
