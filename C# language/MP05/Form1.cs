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

namespace MP05_BieuDoHistogramAnhMauRGB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            Bitmap hinhgoc;
            InitializeComponent();
            // load hinh .pjg tu file 
            // chuyen bien hinh goc thanh bien toan cuc de de su dung cho cac ham khac 
            hinhgoc = new Bitmap(@"E:\Visual Studio\Thi giac may\bird_small.jpg");
            picBox_Hinhgoc.Image = hinhgoc;
            Bitmap Hinhmucxam = ChuyenAnhMauRGBsangHinhXamAverage(hinhgoc);
            picBox_AnhXam.Image = Hinhmucxam;


            // goi cac ham da viet trong bieu do Histogram 
            // tinh histogram 
            double[] histogram = TinhHistogramaAnhXam(Hinhmucxam);
            // chuyen doi kieu du lieu 
            PointPairList points = ChuyenDoiHistogram(histogram);
            // ve bieu do Histogram 
            zG_Histogram.GraphPane=BieuDoHistogram(points);
            zG_Histogram.Refresh();

            // khai bao 3 bien chua 3 kenh mau RGB
            Bitmap red = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap green = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap blue = new Bitmap(hinhgoc.Width, hinhgoc.Height);
        }
        public Bitmap ChuyenAnhMauRGBsangHinhXamAverage(Bitmap hinhgoc)
        {
            Bitmap hinhmauxam = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            for (int x = 0; x < hinhgoc.Width; x++)
            {
                for (int y = 0; y < hinhgoc.Height; y++)
                {
                    // lay diem anh
                    Color pixel = hinhgoc.GetPixel(x, y);
                    byte Red = (byte)pixel.R;
                    byte Green = (byte)pixel.G;
                    byte Blue = (byte)pixel.B;

                    byte Gray = (byte)((Red + Green + Blue) / 3);
                    hinhmauxam.SetPixel(x, y, Color.FromArgb(Gray, Gray, Gray));
                }
            }
            return hinhmauxam;
        }
        // tinh histogram cua anh xam 
        public double[] TinhHistogramaAnhXam(Bitmap Hinhmauxam)
        {   // Moi pixel muc xam co gia tri tu 0-255 , do vay ta khai báo một mảng gồm 256 phần tử dùng để chứa số đếm 
            // của các pixels có cùng mức ảnh xám trong ảnh . 
            // và chúng ta sẽ sử dụng kiểu double vì tổng số đếm lớn và phụ thuộc rất nhiều vào kích thước ảnh 
            double[] histogram = new double[256];
            for(int x =0; x <Hinhmauxam.Width; x++)
            {
                for(int y =0; y < Hinhmauxam.Height; y++)
                {
                    Color color = Hinhmauxam.GetPixel(x,y);
                    byte Gray = color.R;// trong hinh muc xam cac gia tri kenh mau RGB gan nhu giong nhau nen can 1 gtri la du
                    // gia tri gray tinh ra cung chinh la gia tri phan tu trong mang histogram da khai bao . va se lam tang gia tri so dem len 1 
                    histogram[Gray]++;

                }
            }
            return histogram;
        }

        PointPairList ChuyenDoiHistogram(double[] histogram)
        {   // kieu du kieu de ve bieu do cua Zedgraph 
            
            PointPairList points = new PointPairList();
            for(int i=0;i<histogram.Length;i++)
            {   
                // i la tuong ung voi truc nam ngang, tu 0-255 
                // histogram tuong ung voi truc doc , la so pixel cung muc xam 
                points.Add(i, histogram[i]);    
            }
            return points;
        }
        
        // Thiet lap bieu do trong Zedgraph 
        public GraphPane BieuDoHistogram(PointPairList histogram) 
        { 
            // Graghpane la doi tuong trong bieu do ZedGraph
            GraphPane gp = new GraphPane();
            gp.Title.Text = @"Biều Đồ Histogram";
            gp.Rect = new Rectangle(0, 0,600,500); // khung chua bieu do 
            // thiet lap truc ngang 
            gp.XAxis.Title.Text= @"Giá trị mức xám của các điểm ảnh ";
            gp.XAxis.Scale.Min = 0; // nho nhat 0 
            gp.XAxis.Scale.Max = 255; // lon nhat la 255 
            gp.XAxis.Scale.MajorStep = 5; // moi buoc chinh la 5
            gp.XAxis.Scale.MinorStep = 1; // moi buoc nho trong 1 buoc chinh la 1 

            // thiet lap cho truc dung 
            gp.YAxis.Title.Text = @"Số điểm ảnh có cùng mức xám ";
            gp.YAxis.Scale.Min = 0; // nho nhat 0 
            gp.YAxis.Scale.Max = 1500; // số trên phải lớn hơn rất nhiều so với kích thước của ảnh
            gp.YAxis.Scale.MajorStep = 5; // moi buoc chinh la 5
            gp.YAxis.Scale.MinorStep = 1; // moi buoc nho trong 1 buoc chinh la 1 

            // Dùng biểu đồ dạng bar để hiện thị histogram 
            gp.AddBar("Histogram", histogram, Color.OrangeRed);

            return gp;



        }

        private void picBox_Hinhgoc_Click(object sender, EventArgs e)
        {

        }
    }
}
