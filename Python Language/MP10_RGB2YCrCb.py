import cv2
import numpy as np
from PIL import Image

# Khai bao duong dan cho anh mau ban dau
filehinh = r"lena_color.jpg"
imgPIL = Image.open(filehinh)
# doc anh bang thu vien open cv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
# doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)

# tao mot file anh co tuong ung cung kich thuoc va mode voi anh PIL
# anh nay se chua cac ket qua chuyen doi
KY = Image.new(imgPIL.mode, imgPIL.size)
KCr = Image.new(imgPIL.mode,imgPIL.size)
KCb = Image.new(imgPIL.mode,imgPIL.size)
YCrCb_img = Image.new(imgPIL.mode,imgPIL.size)

# lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]

for i in range(width):
    for j in range(height):
        R,G,B = imgPIL.getpixel((i,j))

        Y = np.uint8(16+(65.738/256)*R+(129.057/256)*G+(25.064/256)*B)
        Cr = np.uint8(128-((37.945*R)/256)-((74.494*G)/256)+((112.439*B)/256))
        Cb = np.uint8(128+(((112.439*R)/256)-((94.154*G)/256)-(18.285*B)/256))
        # lay gia tri diem anh

        KY.putpixel((i,j),(Y,Y,Y))
        KCr.putpixel((i,j),(Cr,Cr,Cr))
        KCb.putpixel((i,j),(Cb,Cb,Cb))
        YCrCb_img.putpixel((i,j),(Cb,Cr,Y))

anhY = np.array(KY)
anhCr = np.array(KCr)
anhCb = np.array(KCb)
anhYCrCb = np.array(YCrCb_img)

# Resize cho 4 anh
resize_img = cv2.resize(img,(360,360))
resize_anhY = cv2.resize(anhY,(360,360))
resize_anhCr = cv2.resize(anhCr,(360,360))
resize_anhCb = cv2.resize(anhCb,(360,360))
resize_anhYCrCb = cv2.resize(anhYCrCb,(360,360))
# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",resize_img)
# Hiển thị ảnh mức xám
cv2.imshow("Anh Y ",resize_anhY)
cv2.imshow("Anh Cr ",resize_anhCr)
cv2.imshow("Anh Cb ",resize_anhCb)
cv2.imshow("Anh YCrCb ",resize_anhYCrCb)
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()



