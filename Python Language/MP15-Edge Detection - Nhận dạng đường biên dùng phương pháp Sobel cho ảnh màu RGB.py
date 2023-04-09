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
Sobel_img = Image.new(imgPIL.mode, imgPIL.size)

# lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]

# chon nguong so sanh
nguong = 130
# tao ma tran Sobel theo phuong x,y
Sx = np.array([[-1, -2, -1], [0, 0, 0],[1, 2, 1]])
Sy = np.array([[-1,  0,  1], [-2, 0, 2],[-1,0, 1]])

for x in range(1,width-1):
    for y in range(1,height-1):
        gxx = gyy = gxy = gxR = gxG = gxB = gyR = gyG = gyB = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                gR,gG,gB = imgPIL.getpixel((i,j))
                gxR += gR*  Sx[i - x + 1, j - y + 1]
                gyR += gR*  Sy[i - x + 1, j - y + 1]

                gxG += gG * Sx[i - x + 1, j - y + 1]
                gyG += gG * Sy[i - x + 1, j - y + 1]

                gxB += gB * Sx[i - x + 1, j - y + 1]
                gyB += gB * Sy[i - x + 1, j - y + 1]
        # ap dung ct 6.7-5 den 6.6-7 ta duoc gxx va gyy gxy
        gxx = np.abs(gxR)**2+np.abs(gxG)**2+np.abs(gxB)**2
        gyy = np.abs(gyR)**2+np.abs(gyG)**2+np.abs(gyB)**2
        gxy = (gxR*gyR)+(gxG*gyG)+(gxB*gyB)

        theta = 0.5*np.arctan2((2*gxy),(gxx-gyy))
        F0 = np.sqrt(0.5*(gxx+gyy)+(gxx-gyy)*np.cos(2*theta)+2*gxy*np.sin(2*theta))
        # so sanh gia tri F0 voi gia tri nguong
        if F0 < nguong:
            Sobel_img.putpixel((x,y),(0,0,0))
        else :
            Sobel_img.putpixel((x, y), (255, 255, 255))

# chuyen doi anh tu PIL sang OpenCv
anhSobel = np.array(Sobel_img)

# hien thi thu vien anh dung OpenCV
cv2.imshow("anh hinh goc co gai Lena RGB",img)
cv2.imshow("Nhan dang duong bien bang phuong phap Sobel",anhSobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
