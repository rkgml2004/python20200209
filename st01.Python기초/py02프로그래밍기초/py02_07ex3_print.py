
# 표준출력 print() 에서 줄바꿈을 공백으로 바꾸기

# 디폴트 매개변수
print("a")
print("b")
print("c")
print("d")
print("e")
print("f")
print()
print("a", "\nb", "\nc", "\nd", "\ne", "\nf")
print()
print("a", "b", "c", "d", "e", "f", sep="\n")
print()


# 키워드 매개변수
print("a b c d e f")
print("a", "b", "c", "d", "e", "f")
print("a", end=" ")
print("b", end=" ")
print("c", end=" ")
print("d", end=" ")
print("e", end=" ")
print("f", end=" ")
print()

#
for c in "abcdef":
    print(c, end=" ")
