import cv2
import numpy as np
from PIL import Image

# Nguyen Anh Binh _ 20146097
# Khai bao duong dan cho anh mau ban dau
filehinh1 = r"lena_color.jpg"
filehinh2 = r"bird_small.jpg"
# doc anh bang thu vien open cv
img1 = cv2.imread(filehinh1,cv2.IMREAD_COLOR)
img2 = cv2.imread(filehinh2,cv2.IMREAD_COLOR)
# Doc anh mau dung thu vien PILLOW de xu li va tinh toan thay vi dung OpnenCV
imgPIL1 = Image.open(filehinh1)
imgPIL2 = Image.open(filehinh2)
# tao mot anh co cung kich thuoc va mode voi anh PIL
# Anh nay dung de chua cac ket qua chuyen doi RGB sang Grayscale
binary1 = Image.new(imgPIL1.mode,imgPIL1.size)
binary2 = Image.new(imgPIL2.mode,imgPIL2.size)
# Lay kich thuoc anh PIL1, PIL2
width1 = imgPIL1.size[0]
height1= imgPIL1.size[1]

width2 = imgPIL2.size[0]
height2= imgPIL2.size[1]

# thiet lap gia tri nguong
nguong = 130
# mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
# đọc tất cả các pixel có trong hinh
for x in range(width1):
    for y in range(height1):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL1.getpixel((x,y))

        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Average
        gray1 = np.uint8((R + G + B) / 3)

        # Gan gia tri nhi phan vua tinh duoc cho anh
        if(gray1 < nguong):
            binary1.putpixel((x,y),(0,0,0))
        else:
            binary1.putpixel((x,y),(255,255,255))

for x in range(width2):
    for y in range(height2):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL2.getpixel((x,y))

        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Average
        gray2 = np.uint8((R + G + B) / 3)

        # Gan gia tri nhi phan vua tinh duoc cho anh
        if(gray2 < nguong):
            binary2.putpixel((x, y),(0,0,0))
        else:
            binary2.putpixel((x, y),(255,255,255))

# Chuyen anh PIL sang OpenCv de hien thi bang OpenCV
anhnhiphan_lena=np.array(binary1)
anhnhiphan_lenaresize = cv2.resize(anhnhiphan_lena,(360,360))

anhnhiphan_smallbird=np.array(binary2)
anhnhiphan_smallbirdresize = cv2.resize(anhnhiphan_smallbird,(360,360))


img1_resize = cv2.resize(img1,(360,360))
img2_resize = cv2.resize(img2,(360,360))
# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB Lena ",img1_resize)
cv2.imshow("Anh Mau Goc RGB Small Bird",img2_resize)
# Hiển thị ảnh nhi phan
cv2.imshow("Anh nhi phan Binary Lena",anhnhiphan_lenaresize)
cv2.imshow("Anh nhi phan Binary Small Bird",anhnhiphan_smallbirdresize )
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
