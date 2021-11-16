namespace MayTinhBoTai
{
    partial class MayTinhBoTui
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.labelSoA = new System.Windows.Forms.Label();
            this.labelSoB = new System.Windows.Forms.Label();
            this.textBoxSoA = new System.Windows.Forms.TextBox();
            this.textBoxSoB = new System.Windows.Forms.TextBox();
            this.labelKetQua = new System.Windows.Forms.Label();
            this.textBoxKetQua = new System.Windows.Forms.TextBox();
            this.buttonCong = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // labelSoA
            // 
            this.labelSoA.AutoSize = true;
            this.labelSoA.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelSoA.Location = new System.Drawing.Point(20, 23);
            this.labelSoA.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelSoA.Name = "labelSoA";
            this.labelSoA.Size = new System.Drawing.Size(64, 25);
            this.labelSoA.TabIndex = 0;
            this.labelSoA.Text = "Số a:";
            // 
            // labelSoB
            // 
            this.labelSoB.AutoSize = true;
            this.labelSoB.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelSoB.Location = new System.Drawing.Point(20, 67);
            this.labelSoB.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelSoB.Name = "labelSoB";
            this.labelSoB.Size = new System.Drawing.Size(64, 25);
            this.labelSoB.TabIndex = 1;
            this.labelSoB.Text = "Số b:";
            // 
            // textBoxSoA
            // 
            this.textBoxSoA.Location = new System.Drawing.Point(124, 19);
            this.textBoxSoA.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.textBoxSoA.Name = "textBoxSoA";
            this.textBoxSoA.Size = new System.Drawing.Size(430, 30);
            this.textBoxSoA.TabIndex = 2;
            // 
            // textBoxSoB
            // 
            this.textBoxSoB.Location = new System.Drawing.Point(124, 62);
            this.textBoxSoB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.textBoxSoB.Name = "textBoxSoB";
            this.textBoxSoB.Size = new System.Drawing.Size(430, 30);
            this.textBoxSoB.TabIndex = 3;
            // 
            // labelKetQua
            // 
            this.labelKetQua.AutoSize = true;
            this.labelKetQua.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelKetQua.Location = new System.Drawing.Point(20, 114);
            this.labelKetQua.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelKetQua.Name = "labelKetQua";
            this.labelKetQua.Size = new System.Drawing.Size(94, 25);
            this.labelKetQua.TabIndex = 4;
            this.labelKetQua.Text = "Kết quả:";
            // 
            // textBoxKetQua
            // 
            this.textBoxKetQua.Location = new System.Drawing.Point(124, 106);
            this.textBoxKetQua.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.textBoxKetQua.Name = "textBoxKetQua";
            this.textBoxKetQua.Size = new System.Drawing.Size(430, 30);
            this.textBoxKetQua.TabIndex = 5;
            // 
            // buttonCong
            // 
            this.buttonCong.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonCong.Location = new System.Drawing.Point(124, 146);
            this.buttonCong.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonCong.Name = "buttonCong";
            this.buttonCong.Size = new System.Drawing.Size(121, 36);
            this.buttonCong.TabIndex = 6;
            this.buttonCong.Text = "Cộng";
            this.buttonCong.UseVisualStyleBackColor = true;
            this.buttonCong.Click += new System.EventHandler(this.buttonCong_Click);
            // 
            // MayTinhBoTui
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(13F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 459);
            this.Controls.Add(this.buttonCong);
            this.Controls.Add(this.textBoxKetQua);
            this.Controls.Add(this.labelKetQua);
            this.Controls.Add(this.textBoxSoB);
            this.Controls.Add(this.textBoxSoA);
            this.Controls.Add(this.labelSoB);
            this.Controls.Add(this.labelSoA);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "MayTinhBoTui";
            this.Text = "Máy tính bỏ túi";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label labelSoA;
        private System.Windows.Forms.Label labelSoB;
        private System.Windows.Forms.TextBox textBoxSoA;
        private System.Windows.Forms.TextBox textBoxSoB;
        private System.Windows.Forms.Label labelKetQua;
        private System.Windows.Forms.TextBox textBoxKetQua;
        private System.Windows.Forms.Button buttonCong;
    }
}

