# 중첩 for문

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
print("반복문 없이 출력")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")
print("**********")

print( "--------------------" )

# for 1개를 이용하여 출력
print("for 1개를 이용하여 출력")
for i in range(0, 10, 1):
    print("**********") 

print( "--------------------" )

# for 2개를 이용하여 출력
print("for 2개를 이용하여 출력")
for i in range(1, 11, 1):
    #print("**********") 
    for j in range(1, 11, 1):
        print("*", end="") 
    
    print() # 줄바뀜

print( "--------------------" )

# for 2개를 이용하여 직각 삼각형 출력
print("for 2개를 이용하여 직각 삼각형 출력")
for i in range(1, 11, 1):
    #print("**********") 
    for j in range(1, i+1, 1):
        print("*", end="") 
    
    print() # 줄바뀜

print( "--------------------" )


# for 2개를 이용하여 역삼각형 출력
print("for 2개를 이용하여 역삼각형 출력")
for i in range(1, 11, 1):
    #print("**********") 
    for j in range(1, i+1, 1):
        print(" ", end="") 
    for j in range(i+1, 11, 1):
        print("*", end="")
    
    print() # 줄바뀜

print( "--------------------" )


#         *
#       ***
#     *****
#   *******
# *********
#   *******
#     *****
#       ***
#         *
## 전역 변수 선언 부분 ##
k = 0
i = 0
while i < 9:
    if i < 5:
        k = 0
        while k < 4-i:
            print('  ', end='')
            k += 1
        k = 0
        while k < i*2+1:
            print('*',  end='')
            k += 1
    else:
        k = 0
        while k < i-4:
            print('  ', end='')
            k += 1
        k = 0
        while k < (9-i)*2-1:
            print('*',  end='')
            k += 1
    print()
    i += 1
