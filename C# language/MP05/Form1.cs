using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ZedGraph;
namespace MP05_BieuDoHistogramAnhMauRRGB2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            Bitmap hinhgoc;
            InitializeComponent();
            // chuyen bien hinh goc thanh bien toan cuc de de su dung cho cac ham khac 
            hinhgoc = new Bitmap(@"E:\Visual Studio\Thi giac may\bird_small.jpg");
            picBox_Hinhgoc.Image = hinhgoc;
            // goi cac ham da viet trong bieu do Histogram 
            // tinh histogram cua anh RGB  
            double[,] histogram = TinhHistogramaAnhXam(hinhgoc);
            // chuyen doi kieu du lieu 
            List<PointPairList> points = ChuyenDoiHistogram(histogram);
            // ve bieu do Histogram 
            zG_Histogram.GraphPane = BieuDoHistogram(points);
            zG_Histogram.Refresh();

            // khai bao 3 bien chua 3 kenh mau RGB
            Bitmap red = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap green = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap blue = new Bitmap(hinhgoc.Width, hinhgoc.Height);
        }
        // tinh histogram cua anh mau RGB
        public double[,] TinhHistogramaAnhXam(Bitmap HinhRGB)
        {   // Moi pixel muc xam co gia tri tu 0-255 , do vay ta khai báo một mảng gồm 256 phần tử dùng để chứa số đếm 
            // của các pixels có cùng mức ảnh xám trong ảnh . 
            // và chúng ta sẽ sử dụng kiểu double vì tổng số đếm lớn và phụ thuộc rất nhiều vào kích thước ảnh
            // Chung ta dung mang 2 chieu de chua thong tin histogram cho cac kenh mau RGB 
            // 3 : la so kenh mau can luu , 256 la gia tri tuong ung voi gia tri mau RGB tu 0 den 255 
            double[,] histogram = new double[3, 256];
            for (int x = 0; x < HinhRGB.Width; x++)
            {
                for (int y = 0; y < HinhRGB.Height; y++)
                {
                    Color color = HinhRGB.GetPixel(x, y);
                    byte Red = color.R;
                    byte Green = color.G;
                    byte Blue = color.B;

                    histogram[0, Red]++; // histogram cua kenh mau Do 
                    histogram[1, Green]++; // histogram cua kenh mau xanh
                    histogram[2, Blue]++; // histogram cua kenh mau xanh duong

                }
            }
            return histogram; // tra mang 2 chieu chua thong tin histogram cua 3 gia tri mau RGB 
        }

        List<PointPairList> ChuyenDoiHistogram(double[,] histogram)

        {   // kieu du kieu de ve bieu do cua Zedgraph 
            // dung 1 mang khong can khai bao so luong phan tu de chua cac gia tri chuyen doi 
            List<PointPairList> points = new List<PointPairList>();


            PointPairList redpoints = new PointPairList();// Chuyen doi histogram cho kenh mau Red 
            PointPairList greenpoints = new PointPairList();// Chuyen doi histogram cho kenh mau Green
            PointPairList bluepoints = new PointPairList();// Chuyen doi histogram cho kenh mau Blue


            for (int i = 0; i < 256; i++)
            {
                // i la tuong ung voi truc nam ngang, tu 0-255 
                // histogram tuong ung voi truc doc , la so pixel cung muc xam 
                redpoints.Add(i,histogram[0,i]); // chuyen doi cho kenh mau Red
                greenpoints.Add(i,histogram[1,i]); // chuyen doi cho kenh mau Green
                bluepoints.Add(i,histogram[2,i]); // chuyen doi cho kenh mau Blue
            }
            // sau khi ket thuc vong lap thi thong tin histogram cua cac kenh mau RGB da duoc chuyen doi thanh cong 
            // tiep theo se Add cac kenh mau vao mang points de tra ve cho ham 
            points.Add(redpoints);
            points.Add(greenpoints);
            points.Add(bluepoints);
            return points;
        }

        // Thiet lap bieu do trong Zedgraph 
        public GraphPane BieuDoHistogram(List<PointPairList> histogram)
        {
            // Graghpane la doi tuong trong bieu do ZedGraph
            GraphPane gp = new GraphPane();
            gp.Title.Text = @"Biều Đồ Histogram";
            gp.Rect = new Rectangle(0, 0, 700, 500); // khung chua bieu do 
            // thiet lap truc ngang 
            gp.XAxis.Title.Text = @"Giá trị màu của các điểm ảnh ";
            gp.XAxis.Scale.Min = 0; // nho nhat 0 
            gp.XAxis.Scale.Max = 255; // lon nhat la 255 
            gp.XAxis.Scale.MajorStep = 5; // moi buoc chinh la 5
            gp.XAxis.Scale.MinorStep = 1; // moi buoc nho trong 1 buoc chinh la 1 

            // thiet lap cho truc dung 
            gp.YAxis.Title.Text = @"Số điểm ảnh có cùng giá trị màu ";
            gp.YAxis.Scale.Min = 0; // nho nhat 0 
            gp.YAxis.Scale.Max = 15000; // số trên phải lớn hơn rất nhiều so với kích thước của ảnh
            gp.YAxis.Scale.MajorStep = 5; // moi buoc chinh la 5
            gp.YAxis.Scale.MinorStep = 1; // moi buoc nho trong 1 buoc chinh la 1 

            // Dùng biểu đồ dạng bar để hiện thị histogram 
            gp.AddBar("Histogram's Red", histogram[0], Color.Red);
            gp.AddBar("Histogram's Green", histogram[1], Color.Green);
            gp.AddBar("Histogram's Bule", histogram[2], Color.Blue);

            return gp;

        }
    }
}
