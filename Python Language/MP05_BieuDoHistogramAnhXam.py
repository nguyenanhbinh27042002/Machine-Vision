import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Nguyen Anh Binh _ 20146097

# Doc anh mau dung thu vien PILLOW de xu li va tinh toan thay vi dung OpnenCV

def ChuyenDoiAnhMauSangMauXamLuiminance(imgPIL):
    # tao mot anh co cung kich thuoc va mode voi anh PIL
    # Anh nay dung de chua cac ket qua chuyen doi RGB sang Grayscale
    luiminance = Image.new(imgPIL.mode,imgPIL.size)
    width = imgPIL.size[0]
    height= imgPIL.size[1]
    # mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
    # đọc tất cả các pixel có trong hinh
    for x in range(width):
        for y in range(height):
            # lấy tất cả các giá trị trên điểm ảnh
            R,G,B = imgPIL.getpixel((x,y))
            #Chuyen doi diem anh mau RGB thanh diem muc xam dung phuong phap average
            gray = np.uint8((0.2126 * R + 0.7152 * G + 0.0722 * B))
            # Gan gia tri muc xam vua tinh duoc cho anh xam
            luiminance.putpixel((x,y),(gray,gray,gray))
    # Chuyen anh PIL sang OpenCv de hien thi bang OpenCV
    return luiminance
    #anhmauxam=np.array(average)
def TinhHistogram(HinhXamPIL):
    # tao 1 mang 1 chieu co 256 phan tu, tu 0-255
    histogram = np.zeros(256)
    width2 = HinhXamPIL.size[0]
    height2= HinhXamPIL.size[1]
    for x in range(width2):
        for y in range(height2):
            # lay gia tri xam tai cac diem (x,y)
            gR,gG,gB = HinhXamPIL.getpixel((x,y))

            # gia tri Gray tinh ra duoc cung chinh la phan tu thu Gray co o trong mang tren
            # tang phan tu thu gray len 1 se co mang phan tu thu hisogram
            histogram[gR] += 1
    return histogram
# ham ve bieu do Histogram
def VeBieuDoHistogram(histogram):
    # khai bao chieu dai va chieu rong cua bieu do hien thi
    width2 = 6
    height2 = 5
    plt.figure('Bieu Do Histogram anh xam ',figsize=(((width2,height2))),dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0,256,256)
    plt.plot(trucX,histogram,color='orange')
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
# chuyen sang anh muc xam
HinhXamPIL = ChuyenDoiAnhMauSangMauXamLuiminance(imgPIL)

# tinh histogram
histogram = TinhHistogram(HinhXamPIL)

# chuyen anh tu PIL sang OpenCv de hien thi bang OpenCV cv2
HinhxamCv= np.array(HinhXamPIL)
cv2.imshow("Anh Muc Xam ",HinhxamCv)

# hien thi bieu do Histogram
VeBieuDoHistogram(histogram)

# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
