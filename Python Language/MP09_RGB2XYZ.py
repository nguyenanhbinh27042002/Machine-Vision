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
KX = Image.new(imgPIL.mode, imgPIL.size)
KY = Image.new(imgPIL.mode,imgPIL.size)
KZ = Image.new(imgPIL.mode,imgPIL.size)
XYZ_img = Image.new(imgPIL.mode,imgPIL.size)

# lay kich thuoc cua moi anh
width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        R,G,B = imgPIL.getpixel((x,y))
        # su dung cong thuc de tinh gia tri X,Y,Z
        X = np.uint8(0.4124564*R + 0.3575761*G + 0.1804375*B)
        Y = np.uint8(0.2126729*R + 0.7151522*G + 0.0721750*B)
        Z = np.uint8(0.0193339*R + 0.1191920*G + 0.9503041*B)
# gan gia tri X,Y,Z vua tinh cho hinh
        KX.putpixel((x, y), (X, X, X))
        KY.putpixel((x, y), (Y, Y, Y))
        KZ.putpixel((x, y), (Z, Z, Z))
        XYZ_img.putpixel((x, y), (Z, Y, X))


#hien thi anh tu PIL len openCv
anhX=np.array(KX)
anhY=np.array(KY)
anhZ=np.array(KZ)
anhXYZ=np.array(XYZ_img)
# Resize cho 4 anh
resize_img = cv2.resize(img,(360,360))
resize_anhX = cv2.resize(anhX,(360,360))
resize_anhY = cv2.resize(anhY,(360,360))
resize_anhZ = cv2.resize(anhZ,(360,360))
resize_anhXYZ = cv2.resize(anhXYZ,(360,360))

# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",img)
# Hiển thị ảnh mức xám
cv2.imshow("Anh X ",resize_anhX)
cv2.imshow("Anh Y ",resize_anhY)
cv2.imshow("Anh Z ",resize_anhZ)
cv2.imshow("Anh XYZ ",resize_anhXYZ)
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
