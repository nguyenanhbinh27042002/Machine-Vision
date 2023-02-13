import cv2 #  import thu vien opencv
import numpy as np # import thu vien numpy de cho viec tinh toan
from PIL import Image # import thu vien PILLOW de ho tro nhieu dinh dang anh

# Nguyen Anh Binh _ 20146097
# Khai bao duong dan cho anh mau ban dau
filehinh = r"lena_color.jpg"
# doc anh bang thu vien open cv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)

# Doc anh mau dung thu vien PILLOW de xu li va tinh toan thay vi dung OpnenCV
imgPIL1= Image.open(filehinh)
imgPIL2= Image.open(filehinh)
imgPIL3= Image.open(filehinh)
# tao mot anh co cung kich thuoc va mode voi anh PIL
# Anh nay dung de chua cac ket qua chuyen doi RGB sang Grayscale
average1 = Image.new(imgPIL1.mode,imgPIL1.size)
average2 = Image.new(imgPIL2.mode,imgPIL2.size)
average3 = Image.new(imgPIL3.mode,imgPIL3.size)
# Lay kich thuoc anh PIL
width1 = imgPIL1.size[0]
height1= imgPIL1.size[1]

width2 = imgPIL2.size[0]
height2= imgPIL2.size[1]

width3 = imgPIL3.size[0]
height3= imgPIL3.size[1]
# mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
# đọc tất cả các pixel có trong hinh
for x in range(width2):
    for y in range(height2):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL2.getpixel((x,y))
        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Lightness
        Max = max(R,G,B)
        Min = min(R,G,B)
        gray2 = np.uint8((Min+Max)/2)
        # Gan gia tri muc xam vua tinh duoc cho anh xam
        average2.putpixel((x,y),(gray2,gray2,gray2))

for i in range(width1):
    for j in range(height2):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL1.getpixel((i,j))
        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Average
        gray1 = np.uint8((R + G + B) / 3)
        # Gan gia tri muc xam vua tinh duoc cho anh xam
        average1.putpixel((i,j),(gray1,gray1,gray1))

for m in range(width3):
    for n in range(height3):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL3.getpixel((m,n))
        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Average
        gray3 = np.uint8((0.2126*R + 0.7152*G + 0.0722*B))
        # Gan gia tri muc xam vua tinh duoc cho anh xam
        average3.putpixel((m,n),(gray3,gray3,gray3))

# Chuyen anh PIL sang OpenCv de hien thi bang OpenCV
anhmucxam1=np.array(average1)
anhmucxam2=np.array(average2)
anhmucxam3=np.array(average3)

# Resize cho 4 anh
resize_img = cv2.resize(img,(360,360))
resize_anhmucxam1 = cv2.resize(anhmucxam1,(360,360))
resize_anhmucxam2 = cv2.resize(anhmucxam2,(360,360))
resize_anhmucxam3 = cv2.resize(anhmucxam3,(360,360))

# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",resize_img)
# Hiển thị ảnh mức xám
cv2.imshow("Anh Muc Xam Average",resize_anhmucxam1)
# Hiển thị ảnh mức xám
cv2.imshow("Anh Muc Xam Lightness",resize_anhmucxam2)
# Hiển thị ảnh mức xám
cv2.imshow("Anh Muc Xam Luminance",resize_anhmucxam3)

# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
