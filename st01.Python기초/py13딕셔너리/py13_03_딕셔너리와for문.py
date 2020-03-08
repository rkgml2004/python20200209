# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}


# 딕셔너리 열거
for key in dictionary:
    # 출력합니다.
    print(key, ":", dictionary[key])
print()

# key 만 열거
for key in dictionary.keys():
    print("keys() >>> ", key)
print()

# value 만 열거
for value in dictionary.values():
    print("values() >>> ", value)
print()

# key, value를 쌍으로 열거
for item in dictionary.items():
    print("items() >>> ", item)
print()
