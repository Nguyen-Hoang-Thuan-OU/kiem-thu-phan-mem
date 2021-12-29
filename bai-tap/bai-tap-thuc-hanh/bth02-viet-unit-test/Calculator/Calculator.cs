using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Calculator : Form
    {
        public Calculator()
        {
            InitializeComponent();
        }

        // Nút cộng
        private void buttonPlus_Click(object sender, EventArgs e)
        {
            int firstNumber, secoundNumber;
            Calculation calulation;
            firstNumber = int.Parse(textBoxFirstNumber.Text);
            secoundNumber = int.Parse(textBoxSecondNumber.Text);
            calulation = new Calculation(firstNumber, secoundNumber);
            textBoxResult.Text = calulation.Execute("Plus").ToString();
        }

        // Nút trừ
        private void buttonMinus_Click(object sender, EventArgs e)
        {
            int firstNumber, secoundNumber;
            Calculation calulation;
            firstNumber = int.Parse(textBoxFirstNumber.Text);
            secoundNumber = int.Parse(textBoxSecondNumber.Text);
            calulation = new Calculation(firstNumber, secoundNumber);
            textBoxResult.Text = calulation.Execute("Minus").ToString();
        }

        // Nút nhân
        private void buttonMultiply_Click(object sender, EventArgs e)
        {
            int firstNumber, secoundNumber;
            Calculation calulation;
            firstNumber = int.Parse(textBoxFirstNumber.Text);
            secoundNumber = int.Parse(textBoxSecondNumber.Text);
            calulation = new Calculation(firstNumber, secoundNumber);
            textBoxResult.Text = calulation.Execute("Multiply").ToString();
        }

        // Nút chia
        private void buttonDivide_Click(object sender, EventArgs e)
        {
            int firstNumber, secoundNumber;
            Calculation calulation;
            firstNumber = int.Parse(textBoxFirstNumber.Text);
            secoundNumber = int.Parse(textBoxSecondNumber.Text);
            calulation = new Calculation(firstNumber, secoundNumber);
            textBoxResult.Text = calulation.Execute("Divide").ToString();
        }

        // Nút số mũ
        private void buttonPower_Click(object sender, EventArgs e)
        {
            double firstNumber;
            int secoundNumber;
            double resultPower;
            firstNumber = double.Parse(textBoxFirstNumber.Text);
            secoundNumber = int.Parse(textBoxSecondNumber.Text);
            resultPower = Calculation.Power(firstNumber, secoundNumber);
            textBoxResult.Text = resultPower.ToString();
        }

        private void Calculator_Load(object sender, EventArgs e)
        {

        }
    }
}
