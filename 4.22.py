﻿print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

def is_all_digits_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0: 
            return False
    return True

result = []
for num in range(1000, 3001):
    if is_all_digits_even(num):
        result.append(str(num))

print(",".join(result))
