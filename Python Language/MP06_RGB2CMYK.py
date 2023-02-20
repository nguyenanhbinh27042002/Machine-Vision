import cv2
import numpy as np
from PIL import Image

# Nguyen Anh Binh _ 20146097
# Khai bao duong dan cho anh mau ban dau
filehinh = r"lena_color.jpg"
# doc anh bang thu vien open cv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)

# Doc anh mau dung thu vien PILLOW de xu li va tinh toan thay vi dung OpnenCV
imgPIL = Image.open(filehinh)

width = imgPIL.size[0]
height = imgPIL.size[1]
# tao mot anh co cung kich thuoc va mode voi anh PIL
cyan = Image.new(imgPIL.mode,imgPIL.size)
magenta = Image.new(imgPIL.mode,imgPIL.size)
yellow = Image.new(imgPIL.mode,imgPIL.size)
black = Image.new(imgPIL.mode,imgPIL.size)


# mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
# đọc tất cả các pixel có trong hinh
for x in range(width):
    for y in range (height):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL.getpixel((x,y))
        cyan.putpixel((x,y),(B,G,0))
        magenta.putpixel((x,y),(B,0,R))
        yellow.putpixel((x,y),(0,G,R))
        # lay gia tri min cua RGB
        Min = min(R,G,B)
        K = Min
        black.putpixel((x,y),(K,K,K))
# de hien thi anh qua OpenCv ta phai chuyen doi tu PIL sang OpenCv bang cau lenh
    anh_cyan = np.asarray(cyan)
    anh_magenta = np.asarray(magenta)
    anh_yellow = np.asarray(yellow)
    anh_black = np. asarray(black)

cyan_resize = cv2.resize( anh_cyan,(360,360))
magenta_resize  = cv2.resize(anh_magenta,(360,360))
yellow_resize  = cv2.resize( anh_yellow,(360,360))
black_resize  = cv2.resize(anh_black,(360,360))
# hien thi OpenCv
cv2.imshow('Anh Mau Goc',img)
cv2.imshow('Anh Mau Cyan',cyan_resize )
cv2.imshow('Anh Mau Magenta',magenta_resize )
cv2.imshow('Anh Mau Yellow',yellow_resize )
cv2.imshow('Anh Mau Black',black_resize )
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()