using Emgu.CV.Structure;
using Emgu.CV;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MP01_TachAnhMauRGB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            // tạo một biến nơi chứa đường dẫn lưu hình ảnh gốc RGB cần xử lí 
            // lưu ý :  cần phải @ bởi vì đường dẫn có kí tự đặc biệt chuỗi unicode cho C# hiểu 
            // khai bao bien dinh nghia kieu du lieu cho emgu CV 
     
           // hien thi ket qua luu tu may va trong emgu Cv
            string filehinh = (@"E:\Visual Studio\Thi giac may\lena_color.jpg");

            // tạo một biến chứa hình bitmap từ file đường dẫn lên màn hình hiển thị 
            Bitmap hinhgoc = new Bitmap(filehinh);

            // hiển thị trên image_box hinh gốc dung image box nen xuat hien cau lenh image<bgr
            image_hinhgoc.Image = new Image<Bgr, byte>(hinhgoc);

            // khai báo 3 biến hình bitmap chứa 3 kênh hinh RGB 
            // cung kich thuoc va chieu cao voi hinh goc 
            Bitmap red = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap green = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap blue = new Bitmap(hinhgoc.Width, hinhgoc.Height);

            // mỗi điểm ảnh là một ma trận 2 chiều nên dùng 2 dòng for để quét 
            for (int x = 0; x < hinhgoc.Width;x++) {
                for(int y = 0; y < hinhgoc.Height;y++)
                {
                    // đọc các giá trị pixel tại điểm ảnh có vị trí x y 
                    Color pixel= hinhgoc.GetPixel(x,y);
                    // mỗi pixel gồm 4 giá trị màu bao gồm : độ trong suốt A và R G B 

                    byte R = (byte)pixel.R; // giá trị kênh màu RED
                    byte G = (byte)pixel.G; // giá trị kênh màu GREEN
                    byte B = (byte)pixel.B; // // giá trị kênh màu BLUE
                  
                    // set các giá trị pixel đọc được cho các hình chứa các kênh màu tương ứng RGB
                    red.SetPixel(x,y, Color.FromArgb(R,0,0));
                    green.SetPixel(x,y, Color.FromArgb(0,G,0));
                    blue.SetPixel(x,y, Color.FromArgb(0,0,B));

                }
            }
            // hiển thị 3 hình kênh màu trên pic box đã tạo ra 
            image_RED.Image = new Image<Bgr, byte>(red); 
            image_GREEN.Image = new Image<Bgr, byte>(green);
            image_BLUE.Image = new Image<Bgr, byte>(blue); 
            }
    }
     
}

