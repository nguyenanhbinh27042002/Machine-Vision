import cv2
import numpy as np
# Nguyen Anh Binh _ 20146097
# doc anh bang thu vien open cv
img = cv2.imread("lena_color.jpg",1)   # 1 là trả về ảnh màu bỏ qua kênh màu apha độ trong suốt
                                       # 0 là đọc ảnh trắng đen
                                       #-1 là đoc tất cả các kênh màu (co độ trong suốt anpha)
# lấy kích thước của ảnh da duoc load
height = len(img[0])
width = len(img[0])

# khai báo biến chứa 3 biến kênh màu RGB
red = np.zeros((height,width,3),np.uint8) # số 3 là 3 kênh màu RGB, mỗi kênh 8bit
blue = np.zeros((height,width,3),np.uint8)
green = np.zeros((height,width,3),np.uint8)

# bắt đầu set zero cho 3 kênh màu hien thi RGB
red[:] = [0,0,0]
blue[:] = [0,0,0]
green[:] = [0,0,0]

# mỗi ảnh đều là một ma trận 2 chiều nên sử dụng 2 dòng for
# đọc tất cả các pixel có trong hinh
for x in range(0,width):
    for y in range(0,height):
        # lấy tất cả các giá trị trên điểm ảnh
        R =img[x,y,2]
        B = img[x,y,1]
        G = img[x,y,0]
        # Thiết lập các màu cho các kênh
        red[x,y,2] = R
        blue[x,y,1] = B
        green[x,y,0] = G


# Nối tất cả các hình lại với nhau theo chiêu ngang
vert1 = np.concatenate((img,blue),axis=0)
vert2 = np.concatenate((red,green), axis=0)
# Dieu chinh kich thuoc cua 4 anh
c = cv2.resize(vert1,(250,250))
d = cv2.resize(vert2,(250,250))
 #Ket noi anh theo chieu doc
horiz = np.concatenate((c,d), axis=1)
f= cv2.resize(horiz,(700,700))

#Hiện thị ảnh dùng thư viện OpenCv
cv2.imshow("Tach Anh Mau RGB",f)
# bam phim bat ki de hien thi
k=cv2.waitKey(0)
# giai phong bo nho da cap phat cho cac cửa sổ đã hiển thị
cv2.destroyAllWindows()
