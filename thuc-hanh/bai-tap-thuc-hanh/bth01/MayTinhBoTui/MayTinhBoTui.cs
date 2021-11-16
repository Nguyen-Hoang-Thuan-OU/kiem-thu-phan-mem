using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MayTinhBoTai
{
    public partial class MayTinhBoTui : Form
    {
        public MayTinhBoTui()
        {
            InitializeComponent();
        }

        private void buttonCong_Click(object sender, EventArgs e)
        {
            if (textBoxSoA.Text != String.Empty)
            {
                double a = double.Parse(textBoxSoA.Text);
                double b = double.Parse(textBoxSoB.Text);
                double c = a + b;
                textBoxKetQua.Text = c.ToString();
            }
        }

        private void buttonTru_Click(object sender, EventArgs e)
        {
            double a = double.Parse(textBoxSoA.Text);
            double b = double.Parse(textBoxSoB.Text);
            double c = a - b;
            textBoxKetQua.Text = c.ToString();
        }
    }
}
