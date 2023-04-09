import cv2
import numpy as np
from PIL import Image
import math

# Khai bao duong dan cho anh mau ban dau
filehinh = r"lena_color.jpg"
imgPIL = Image.open(filehinh)
# doc anh bang thu vien open cv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
# doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)

# tao mot file anh co tuong ung cung kich thuoc va mode voi anh PIL
# anh nay se chua cac ket qua chuyen doi
Hue = Image.new(imgPIL.mode, imgPIL.size)
Staturation = Image.new(imgPIL.mode,imgPIL.size)
Value = Image.new(imgPIL.mode,imgPIL.size)
HSV_img = Image.new(imgPIL.mode,imgPIL.size)

# lay kich thuoc cua moi anh
width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        R,G,B = imgPIL.getpixel((x,y))
        Min = min(R,G,B)
        Sum = (R+G+B)
        Max = max(R,G,B)
        # ap dung cong thuc trong sach
        # t1 la phan tu dau tien o tren tu cua cong thuc
        t1 = ((R-G)+(R-B))/2
        # t2 la phan tu dau tien o duoi mau cua cong thuc
        t2  = math.sqrt((R-G)*(R-G)+(R-B)*(G-B))

        # chu y la ham trong phep tinh Acos trong cong thuc la radian
        thelta = math.acos(t1/t2)
        # cong thuc tinh gia tri hue
        h = 0
        # Neu ma B <= G thi thelta = hue
        if B <= G:
            h = thelta
        else:
            # neu ma B > G thi thelta = 360 - hue
            h = 2*math.pi - thelta
        # do thelta tinh ra gia tri la radian nen ta tinh ra gia tri pi thay vi la 360
        # chuyen doi gia tri radian sang gia tri pi
        h=np.uint8(h*180/math.pi)

        # cong thuc tinh gia tri Staturation
        s = 1-3*Min/Sum
        s = np.uint8(s*255)
        # do gia tri cua sta la tu 0 den 1 nen chung ta can phai chuyen doi sang gia tri la 1 byte
        # tu 0-255

        # cong thuc tinh Value
        v = np.uint8(Max)

        Hue.putpixel((x, y), (h, h, h))
        Staturation.putpixel((x, y), (s, s, s))
        Value.putpixel((x, y), (v, v, v))
        HSV_img.putpixel((x, y), (v, s, h))


# Chuyen anh PIL sang OpenCv de hien thi bang OpenCV
anhH=np.array(Hue)
anhS =np.array(Staturation)
anhV =np.array(Value)
anhHSV=np.array(HSV_img)

# Resize cho 4 anh
resize_img = cv2.resize(img,(360,360))
resize_anhH = cv2.resize(anhH,(360,360))
resize_anhS = cv2.resize(anhS,(360,360))
resize_anhV = cv2.resize(anhV,(360,360))
resize_anhHSV = cv2.resize(anhHSV,(360,360))

# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",resize_img)
cv2.imshow("Anh Mau Kenh Hue",resize_anhH)
cv2.imshow("Anh Mau Kenh Staturation",resize_anhS)
cv2.imshow("Anh Mau kenh Value ",resize_anhV)
cv2.imshow("Anh Mau HSV ",resize_anhHSV)

#bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()