using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MP06_RGB2CMYK
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Bitmap hinhgoc = new Bitmap(@"E:\Visual Studio\Thi giac may\lena_color.jpg");

            // cho hien thi tren hinh tren pictureBox
            picBox_Hinhgoc.Image = hinhgoc;
            // goi ham de xu li chuyen doi kenh mau RGB sang CYMK 
            // hien thi cac kenh mau CMYK duoc chuyen doi tu RGB 
            List<Bitmap> CYMK = ChuyenDoiAnhRGBSangCYMK(hinhgoc);

            // ham trên trả về 4 giá trị tương ứng CYMK 
            picBox_KenhCyan.Image = CYMK[0]; // kenh mau Cyan
            picBox_KenhMagenta.Image = CYMK[1]; // kenh mau Magenta
            picBox_KenhYellow.Image = CYMK[2]; // kenh mau Yellow
            picBox_KenhBlack.Image = CYMK[3]; // kenh mau Black
        }

       public List<Bitmap> ChuyenDoiAnhRGBSangCYMK( Bitmap hinhgoc) {
            /*  chuyen doi mau RGB sang CYMK la su ket hop giua cac mau cua cac kenh tuong ung nhu : 
             Mau xanh (Cyan) : la su ket hop cua mau Green va Blue , vi the set kenh mau RED = 0 
             Mau Magenta(tim) : la su ket hop cua mau Red va blue , vi the ser kenh mau Green = 0 
             Mau Yellow : la su ket hop cua mau Red va Green vi the ser kenh mau Blue = 0 
             Con mau den (black) la su đơn gian min(R,G,B) */ 
            
            // Tạo một list gồm 4 kênh mau tuong ung CMYK 
            List<Bitmap> CYMK = new List<Bitmap>();
            Bitmap Cyan = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap Magenta = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap Yellow = new Bitmap(hinhgoc.Width, hinhgoc.Height);
            Bitmap Black = new Bitmap(hinhgoc.Width, hinhgoc.Height);


            for(int x = 0;x<hinhgoc.Width;x++)
            {
                for(int y = 0; y < hinhgoc.Height; y++)
                {
                    // lay diem anh 
                    Color pixel = hinhgoc.GetPixel(x, y);
                    byte Red = pixel.R;
                    byte Green = pixel.G;
                    byte Blue = pixel.B;

                    // Mau xanh (Cyan) : la su ket hop cua mau Green va Blue , vi the set kenh mau RED = 0 
                    Cyan.SetPixel(x, y, Color.FromArgb(0, Green, Blue));

                    // Mau Magenta(tim) : la su ket hop cua mau Red va blue , vi the ser kenh mau Green = 0 
                    Magenta.SetPixel(x, y, Color.FromArgb(Red,0, Blue));

                    // Mau Yellow : la su ket hop cua mau Red va Green vi the ser kenh mau Blue = 0 
                    Yellow.SetPixel(x, y, Color.FromArgb(Red, Green,0));

                    // Màu Black la su đơn gian min(R,G,B)
                    byte K = Math.Min(Red, Math.Min(Green, Blue)); // Do ham min chi co 2 sô nên phải thực hiện 2 lân tính toán min 
                    Black.SetPixel(x, y, Color.FromArgb(K, K, K));
                }
                // Add cac hinh tuong ung cac kenh mau CMYK vao list 
                // Do list là kiểu dữ liệu mảng nên không cần biết trước kích thước nên minh có thê Add các phép tính vào trong list
                // mà không cần quan tâm là có bị tràn hay không 
                CYMK.Add(Cyan);
                CYMK.Add(Magenta);
                CYMK.Add(Yellow);
                CYMK.Add(Black);
            }
            return CYMK;
        }
    }
}
