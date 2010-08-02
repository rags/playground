using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace LINQDemo
{
    public partial class Form1 : Form
    {
        
        public Form1()
        {
            InitializeComponent();

            setUp1xClickhandler();
            setUp20ClickHandler();
            setup30ClickHandler();
        }

        private void setUp1xClickhandler()
        {
            btn1x.Click  += new EventHandler(Click_);
        }

        private void Click_(object sender, EventArgs e)
        {
            MessageBox.Show(((Button) sender).Text);
        }

        private void setUp20ClickHandler()
        {
            btn20.Click +=  delegate(object sender, EventArgs e)
                                  {
                                      MessageBox.Show(((Button) sender).Text);
                                  };
        }

        private void setup30ClickHandler()
        {
            btn30.Click += (sender,e)=> MessageBox.Show(((Button) sender).Text);
        }


        public static void Main()
        {
            new Form1().ShowDialog();
        }
      
    }
}