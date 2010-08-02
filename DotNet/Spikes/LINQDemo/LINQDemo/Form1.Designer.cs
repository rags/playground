using System.Windows.Forms;

namespace LINQDemo
{
    partial class Form1
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
            this.btn1x = new Button();
            this.btn20 = new Button();
            this.btn30 = new Button();
            this.SuspendLayout();
            // 
            // btn1x
            // 
            this.btn1x.Location = new System.Drawing.Point(21, 21);
            this.btn1x.Name = "btn1x";
            this.btn1x.Size = new System.Drawing.Size(245, 60);
            this.btn1x.TabIndex = 0;
            this.btn1x.Text = "1.x";
            this.btn1x.UseVisualStyleBackColor = true;
            // 
            // btn20
            // 
            this.btn20.Location = new System.Drawing.Point(24, 106);
            this.btn20.Name = "btn20";
            this.btn20.Size = new System.Drawing.Size(245, 60);
            this.btn20.TabIndex = 1;
            this.btn20.Text = "2.0";
            this.btn20.UseVisualStyleBackColor = true;
            // 
            // btn30
            // 
            this.btn30.Location = new System.Drawing.Point(26, 189);
            this.btn30.Name = "btn30";
            this.btn30.Size = new System.Drawing.Size(245, 60);
            this.btn30.TabIndex = 2;
            this.btn30.Text = "3.0";
            this.btn30.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 273);
            this.Controls.Add(this.btn30);
            this.Controls.Add(this.btn20);
            this.Controls.Add(this.btn1x);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private Button btn1x;
        private Button btn20;
        private Button btn30;
    }
}