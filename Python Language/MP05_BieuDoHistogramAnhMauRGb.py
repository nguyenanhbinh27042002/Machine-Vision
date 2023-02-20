import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Nguyen Anh Binh _ 20146097
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Nguyen Anh Binh _ 20146097

# Doc anh mau dung thu vien PILLOW de xu li va tinh toan thay vi dung OpnenCV
def TinhHistogram(imgPIL):
    # tao 1 mang 1 chieu co 256 phan tu, tu 0-255
    histogram1 = np.zeros(256)
    histogram2 = np.zeros(256)
    histogram3 = np.zeros(256)
    width2 = imgPIL.size[0]
    height2= imgPIL.size[1]
    for x in range(width2):
        for y in range(height2):
            # lay gia tri xam tai cac diem (x,y)
            gR,gG,gB = imgPIL.getpixel((x,y))

            # gia tri Gray tinh ra duoc cung chinh la phan tu thu Gray co o trong mang tren
            # tang phan tu thu gray len 1 se co mang phan tu thu hisogram
            histogram1[gR] += 1
            histogram2[gG] += 1
            histogram3[gB] += 1
    return histogram1, histogram2, histogram3
# ham ve bieu do Histogram
def VeBieuDoHistogram(histogram1, histogram2, histogram3):
    # khai bao chieu dai va chieu rong cua bieu do hien thi
    width2 = 6
    height2 = 5
    plt.figure('Bieu Do Histogram anh xam ',figsize=(((width2,height2))),dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0,256,256)
    plt.plot(trucX,histogram1,color='red')
    plt.plot(trucX, histogram2, color='green')
    plt.plot(trucX, histogram3, color='blue')
    plt.title('Biều đồ Histogram anh xam')
    plt.xlabel('Giá trị mức xam ')
    plt.ylabel('Số điểm cùng giá trị muc xám ')
    plt.show()



# Khai bao duong dan cho anh mau ban dau
filehinh = r"bird_small.jpg"
imgPIL = Image.open(filehinh)
# doc anh bang thu vien open cv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
# Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Anh Mau Goc RGB",img)
# doc anh tu thu vien PIL
imgPIL = Image.open(filehinh)

# tinh histogram
histogram1,histogram2,histogram3 = TinhHistogram(imgPIL)

# hien thi bieu do Histogram
VeBieuDoHistogram(histogram1,histogram2,histogram3)

# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()

