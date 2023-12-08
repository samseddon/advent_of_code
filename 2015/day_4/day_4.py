import hashlib


key = "abcdef"
key = "pqrstuv"
key = "bgvyzdsv"
number = 0
result = hashlib.md5(bytes(key + str(number), encoding='utf-8'))               
five = result.hexdigest()[:5]  
while five != "000000":
    result = hashlib.md5(bytes(key + str(number), encoding='utf-8'))
    five = result.hexdigest()[:6]
    number += 1

print(five, number-1)

