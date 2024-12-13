print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

chuoi = input('Nhap chuoi: ')
chuoi_moi = ''.join([ki_tu for ki_tu in chuoi if not ki_tu.isdigit()])
print('Chuoi sau khi loai b chu so:', chuoi_moi)
