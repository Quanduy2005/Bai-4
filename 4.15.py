﻿print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

chuoi = input('Nhập chuỗi cac tu tieng anh: ')
ds_list = chuoi.split()
ds_list.sort()
print('cac tu theo thu tu tu dien:')
for tu in ds_list:
    print(tu)