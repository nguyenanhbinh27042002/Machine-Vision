using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MP03_ChuyenAnhMauRGBSangAnhMauXam
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            string filehinh = (@"E:\Visual Studio\Thi giac may\lena_color.jpg");
            Bitmap hinhgoc = new Bitmap(filehinh);
            picBox_Hinhgoc.Image= hinhgoc;
            picBox_HinhAnhAverage.Image = ChuyenAnhMauRGBsangHinhXamAverage(hinhgoc);
            picBox_AnhXamLigtness.Image = ChuyenAnhMauRGBsangHinhXamLightness(hinhgoc);
            picBox_AnhXamLuminance.Image = ChuyenAnhMauRGBsangHinhXamLuminance(hinhgoc);

            // khai bao 3 bien chua 3 kenh mau RGB
            Bitmap red = new Bitmap(hinhgoc.Width,hinhgoc.Height);
            Bitmap green = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap blue = new Bitmap(hinhgoc.Width, hinhgoc.Height);
        }
        //tao ham average
        public Bitmap ChuyenAnhMauRGBsangHinhXamAverage(Bitmap hinhgoc) 
        {
            Bitmap hinhmauxam = new Bitmap(hinhgoc.Width,hinhgoc.Height);
            for(int x = 0; x < hinhgoc.Width; x++)
            {
                for (int y = 0; y < hinhgoc.Height; y++) 
                {   
                    // lay diem anh
                    Color pixel = hinhgoc.GetPixel(x,y);
                    byte Red = (byte)pixel.R;
                    byte Green = (byte)pixel.G;
                    byte Blue = (byte)pixel.B;

                    byte Gray= (byte)((Red+Green+Blue)/3);
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
                    Color pixel = hinhgoc.GetPixel(x,y);
                    byte Red = (byte)pixel.R;
                    byte Green = (byte)pixel.G;
                    byte Blue = (byte)pixel.B;

                    byte Max = Math.Max(Red,Math.Max(Green, Blue));
                    byte Min = Math.Min(Red, Math.Min(Green, Blue));
                    byte Gray = (byte)((Max+Min)/2);
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
                    Color pixel = hinhgoc.GetPixel(x,y);
                    byte Red = (byte)pixel.R;
                    byte Green = (byte)pixel.G;
                    byte Blue = (byte)pixel.B;

                    byte Gray = (byte)(0.2126*Red + 0.7152*Green + 0.0722*Blue);
                    hinhmauxam.SetPixel(x, y, Color.FromArgb(Gray, Gray, Gray));
                }
            }

            return hinhmauxam;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
