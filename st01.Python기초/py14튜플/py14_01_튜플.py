# 이메일을 입력 받고 @를 기준으로 id와 도메인을 분리하는 프로그램을 작서하시오.
# 예시) abc@naver.com  --> id: abc  , domain: naver.com

address=input('이메일 주소를 입력하시오: ')


(id, domain) = address.split('@')
print(address)
print('     '+id)
print('     '+domain)

arr = address.split('@')
(id, domain) = arr # id = arr[0], domain = arr[1]  
print(address)
print('     '+id)
print('     '+domain)
