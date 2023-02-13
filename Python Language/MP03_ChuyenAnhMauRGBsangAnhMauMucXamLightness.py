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

# tao mot anh co cung kich thuoc va mode voi anh PIL
# Anh nay dung de chua cac ket qua chuyen doi RGB sang Grayscale
average = Image.new(imgPIL.mode,imgPIL.size)

# Lay kich thuoc anh PIL
width = imgPIL.size[0]
height= imgPIL.size[1]

# mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
# đọc tất cả các pixel có trong hinh
for x in range(width):
    for y in range(height):
        # lấy tất cả các giá trị trên điểm ảnh
        R,G,B = imgPIL.getpixel((x,y))

        # Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap Lightness
        Max = max(R,G,B)
        Min = min(R,G,B)
        gray = np.uint8((Min+Max)/2)

        # Gan gia tri muc xam vua tinh duoc cho anh xam
        average.putpixel((x,y),(gray,gray,gray))

# Chuyen anh PIL sang OpenCv de hien thi bang OpenCV
anhmucxam=np.array(average)

# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",img)
# Hiển thị ảnh mức xám
cv2.imshow("Anh Muc Xam Lightness",anhmucxam)

# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
