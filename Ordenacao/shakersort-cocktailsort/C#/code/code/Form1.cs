using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace code
{
    public partial class Form : System.Windows.Forms.Form
    {
        public Form()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Label1_Click(object sender, EventArgs e)
        {

        }

        private void ListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Cocktail(int[] lista)
        {
            Boolean houveTroca;

            do
            {
                houveTroca = false;
                for (int i = 0; i < lista.Length - 1; i++)
                {
                    if (lista[i] > lista[i + 1])
                    {
                        int temp = lista[i];
                        lista[i] = lista[i + 1];
                        lista[i + 1] = temp;
                        houveTroca = true;
                    }
                }

                for (int i = lista.Length - 1; i > 0; i--)
                {
                    if (lista[i] < lista[i - 1])
                    {
                        int temp = lista[i];
                        lista[i] = lista[i - 1];
                        lista[i - 1] = temp;
                        houveTroca = true;
                    }
                }

            } while (houveTroca);
        }

        private void Gerar_Click(object sender, EventArgs e)
        {
            int[] lista = new int[5];
            Random randNum = new Random();

            for (int i = 0; i < 5; i++)
            {
                lista[i] = randNum.Next(20);
            }

            Cocktail(lista);
            listBox1.Items.Clear();

            for (int i = 0; i < lista.Length; i++)
            {
                listBox1.Items.Add(lista[i]);
            }

        }
    }
}
