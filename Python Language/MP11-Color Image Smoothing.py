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
smooth3 = Image.new(imgPIL.mode, imgPIL.size)
smooth5 = Image.new(imgPIL.mode, imgPIL.size)
smooth7 = Image.new(imgPIL.mode, imgPIL.size)
smooth9 = Image.new(imgPIL.mode, imgPIL.size)

# lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]

# ma tran 3x3 co the bo qua cac vien ngoai cua anh
# nen width = width - 1 ; height = heigtht - 1
for x in range(1,width-1):
    for y in range(1,height-1):
        # lay gia tri diem anh tai vi tri x,y
        # bien nay se chua cac gia tri cong don trong mat na
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                # lay thong tin mau RGB
                R, G, B = imgPIL.getpixel((i, j))
                Rs += R
                Gs += G
                Bs += B
                # ket thuc quet lay gia tri cong don trong mat na
                K = 3 * 3
        Rs = np.uint8(Rs / K)
        Gs = np.uint8(Gs / K)
        Bs = np.uint8(Bs / K)
        smooth3.putpixel((x,y), (Bs, Gs, Rs))

# ma tran 5x5 co the bo qua cac vien ngoai cua anh
# nen width = width - 2 ; height = heigtht - 2
for x in range(2,width-2):
    for y in range(2,height-2):
        # lay gia tri diem anh tai vi tri x,y
        # bien nay se chua cac gia tri cong don trong mat na
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                # lay thong tin mau RGB
                R,G,B = imgPIL.getpixel((i,j))
                Rs +=R
                Gs +=G
                Bs +=B
                # ket thuc quet lay gia tri cong don trong mat na
                K = 5*5
        Rs =np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs =np.uint8(Bs/K)
        smooth5.putpixel((x,y),(Bs,Gs,Rs))

# ma tran 7x7 co the bo qua cac vien ngoai cua anh
# nen width = width - 3 ; height = heigtht - 3
for x in range(3,width-3):
    for y in range(3,height-3):
        # lay gia tri diem anh tai vi tri x,y
        # bien nay se chua cac gia tri cong don trong mat na
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-3,x+4):
            for j in range(y-3,y+4):
                # lay thong tin mau RGB
                R,G,B = imgPIL.getpixel((i,j))
                Rs +=R
                Gs +=G
                Bs +=B
                # ket thuc quet lay gia tri cong don trong mat na
                K = 7*7
        Rs =np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs =np.uint8(Bs/K)
        smooth7.putpixel((x,y),(Bs,Gs,Rs))

# ma tran 9x9 co the bo qua cac vien ngoai cua anh
# nen width = width - 4 ; height = heigtht - 4
for x in range(4, width - 4):
        for y in range(4, height - 4):
            # lay gia tri diem anh tai vi tri x,y
            # bien nay se chua cac gia tri cong don trong mat na
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x - 4, x +5 ):
                for j in range(y - 4, y + 5):
                    # lay thong tin mau RGB
                    R, G, B = imgPIL.getpixel((i, j))
                    Rs += R
                    Gs += G
                    Bs += B
                    # ket thuc quet lay gia tri cong don trong mat na
                    K = 9 * 9
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)
            smooth9.putpixel((x, y), (Bs, Gs, Rs))

anh3x3 =np.array(smooth3)
anh5x5 =np.array(smooth5)
anh7x7 =np.array(smooth7)
anh9x9 =np.array(smooth9)
resize_img = cv2.resize(img,(360,360))
resize_anh3x3 = cv2.resize(anh3x3,(360,360))
resize_anh5x5 = cv2.resize(anh5x5,(360,360))
resize_anh7x7 = cv2.resize(anh7x7,(360,360))
resize_anh9x9 = cv2.resize(anh9x9 ,(360,360))

# Hiển thị ảnh mức xám
cv2.imshow("Anh 3x3 ",resize_anh3x3)
cv2.imshow("Anh 5x5 ",resize_anh5x5)
cv2.imshow("Anh 7x7 ",resize_anh7x7)
cv2.imshow("Anh 9x9 ",resize_anh9x9)
cv2.imshow("Anh Goc ",resize_img)

# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()