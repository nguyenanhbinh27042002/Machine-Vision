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

# tao mot file anh co kich thuoc tuong ung
# anh nay se dung de chuyen doi gia tri RGB sang GrayScale
anhXam = Image.new(imgPIL.mode, imgPIL.size)
Sobel_img = Image.new(imgPIL.mode, imgPIL.size)

# lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        R,G,B = imgPIL.getpixel((x,y))
        # dung cong thuc Average de chuyen doi anh Xam
        gray = np.uint8((R+G+B)/3)
        anhXam.putpixel((x,y),(gray,gray,gray))
nguong = 130
# tao ma tran Sobel theo phuong x,y
Sx = np.array([[-1, -2, -1], [0, 0, 0],[1, 2, 1]])
Sy = np.array([[-1,  0,  1], [-2, 0, 2],[-1,0, 1]])
# sau khi tinh gia tri sobel ta se su dung vung anh 3x3 de tinh toan
# dong thoi se nhan voi ma tran Sobel lan luot theo phuong x ,y de tinh ra duoc gx,gy
for x in range(1,width-1):
    for y in range(1,height-1):
        gx=gy=0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                gR,gG,gB = anhXam.getpixel((i,j))
                gx+=gR*Sx[i-x+1,j-y+1]
                gy+=gR*Sy[i-x+1,j-y+1]
        #tinh gia tri bien do theo Ct 2.20 nham giam thoi gian lam viec cho CPU
        M=np.abs(gx)+np.abs(gy)
        # so sanh gia tri M(x,y) voi gia tri nguong
        if M< nguong :
            Sobel_img.putpixel((x,y),(0,0,0))
        else :
            Sobel_img.putpixel((x,y),(255,255,255))
# chuyen doi anh tu PIL sang OpenCv
anhSobel = np.array(Sobel_img)

# hien thi thu vien anh dung OpenCV
cv2.imshow("anh hinh goc co gai Lena RGB",img)
cv2.imshow("Nhan dang duong bien anh xam Average",anhSobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
