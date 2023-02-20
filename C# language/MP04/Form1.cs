using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MP04_ChuyenAnhMauRGBSangNhiPhan
{
    public partial class Form1 : Form
    {
        Bitmap hinhgoc;
        public Form1()
        {
            
            InitializeComponent();
            // load hinh .pjg tu file 
            // chuyen bien hinh goc thanh bien toan cuc de de su dung cho cac ham khac 
            hinhgoc = new Bitmap(@"E:\Visual Studio\Thi giac may\lena_color.jpg");
            pictBox_Hinhgoc.Image = hinhgoc;
            HinhAnhAverage.Image = ChuyenAnhMauRGBsangHinhXamAverage(hinhgoc);
            picbox_AnhXamLigtness.Image = ChuyenAnhMauRGBsangHinhXamLightness(hinhgoc);
            picBox_AnhxamLuiminance.Image = ChuyenAnhMauRGBsangHinhXamLuminance(hinhgoc);
            // tinh hinh nhi phan 
            picBox_HinhNhiPhan.Image = ChuyenAnhMauRGBsangHinhNhiPhan(hinhgoc,130);


            // khai bao 3 bien chua 3 kenh mau RGB
            Bitmap red = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap green = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap blue = new Bitmap(hinhgoc.Width, hinhgoc.Height);
        }

        //tao ham average
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
        // tao ham chuyen anh RGB sang anh xam Lightness
        public Bitmap ChuyenAnhMauRGBsangHinhXamLightness(Bitmap hinhgoc)
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

                    byte Max = Math.Max(Red, Math.Max(Green, Blue));
                    byte Min = Math.Min(Red, Math.Min(Green, Blue));
                    byte Gray = (byte)((Max + Min) / 2);
                    hinhmauxam.SetPixel(x, y, Color.FromArgb(Gray, Gray, Gray));
                }
            }

            return hinhmauxam;
        }
        //Luminance
        public Bitmap ChuyenAnhMauRGBsangHinhXamLuminance(Bitmap hinhgoc)
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

                    byte Gray = (byte)(0.2126 * Red + 0.7152 * Green + 0.0722 * Blue);
                    hinhmauxam.SetPixel(x, y, Color.FromArgb(Gray, Gray, Gray));
                }
            }
            return hinhmauxam;
        }
        public Bitmap ChuyenAnhMauRGBsangHinhNhiPhan(Bitmap hinhgoc, byte nguong)
        {
            Bitmap hinhnhiphan = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            for (int x = 0; x < hinhgoc.Width; x++)
            {
                for (int y = 0; y < hinhgoc.Height; y++)
                {
                    // lay diem anh
                    Color pixel = hinhgoc.GetPixel(x, y);
                    byte Red = (byte)pixel.R;
                    byte Green = (byte)pixel.G;
                    byte Blue = (byte)pixel.B;

                    byte nhiphan = (byte)(0.2126 * Red + 0.7152 * Green + 0.0722 * Blue);

                    // phan loai diem anh pixel sang nhi phan dua tren gia tri nguong
                    if (nhiphan < nguong)
                        nhiphan = 0;
                    else nhiphan = 255;
                    hinhnhiphan.SetPixel(x, y, Color.FromArgb(nhiphan, nhiphan, nhiphan));

                }
            }
            return hinhnhiphan;
        }
        private void ScrollBar_nguong_valuechanged(object sender, EventArgs e)
        {
            // lay gia tri nguong tu gia tri thanh cuon 
            // Do gia tri cua thanh cuon la int ma nguong do la byte nen ta phai ep kieu int, ve byte 

            byte nguong = (byte)ScrollBar_nguong.Value;
            // cho hien gia tri cua nguong 
            lbl_nguong.Text= nguong.ToString();
            // goi ham nhi phan cho hien thi 
            picBox_HinhNhiPhan.Image = ChuyenAnhMauRGBsangHinhNhiPhan(hinhgoc, nguong);
        }

       

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
    }
    
