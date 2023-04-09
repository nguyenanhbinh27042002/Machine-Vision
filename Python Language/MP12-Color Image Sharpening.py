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
SharpImg = Image.new(imgPIL.mode, imgPIL.size)
# ma tran thay the de tinh cho phuong phap laplitcian
matrix =([[0,-1,0],[-1,4,-1],[0,-1,0]])


# lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]

# tan dung ma na 3x3 , vi day la mat na 3x3 nen chung ta se bo qua dien vien ngoai trong hinh goc
# nen width = width - 1 ; height = heigtht - 1
for x in range(1,width-1):
    for y in range(1,height-1):
        # lay gia tri diem anh tai vi tri x,y
        # bien nay se chua cac gia tri cong don trong mat na
        Rs = 0
        Gs = 0
        Bs = 0

        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                # lay thong tin mau RGB
                R,G,B = imgPIL.getpixel((i,j))
                R += Rs*matrix[i-x+1][j-y+1]
                G += Gs*matrix[i-x+1][j-y+1]
                B += Bs*matrix[i-x+1][j-y+1]
                # ket thuc quet lay gia tri cong don trong mat na
                # tinh diem sac net moi kenh mau theo cong thuc 3.6.7
        R1,G1,B1 = imgPIL.getpixel((x,y))
        sharpR = R1 + Rs
        sharpG = G1 + Gs
        sharpB = B1 + Bs
        # song sanh gia tri kenh mau do da cong don trong mat na
        if   sharpR < 0:
             sharpR = 0
        elif sharpR > 255:
             sharpR = 255

        # song sanh gia tri kenh mau xanh da cong don trong mat na
        if   sharpG < 0:
             sharpG = 0
        elif sharpG > 255:
             sharpG = 255
        # song sanh gia tri kenh mau xanh bien da cong don trong mat na
        if   sharpB < 0:
             sharpB = 0
        elif sharpB > 255:
             sharpB = 255
        SharpImg.putpixel((x,y),(sharpB,sharpG,sharpR))


anhSharp =np.array(SharpImg)
cv2.imshow("Anh Goc ",img)
cv2.imshow("Anh Sharp ",anhSharp)
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()