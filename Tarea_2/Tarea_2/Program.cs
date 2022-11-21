using System;

namespace Tarea_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Escribe un numero: ");
            int num = Convert.ToInt32(Console.ReadLine());

            Tabla(num);
        }

        static void Tabla(int num)
        {
            for(int i = 1; i <= 10; i++) 
            {
                Console.WriteLine(num + " x " + i + " = " + num * i);
            }
        }
    }
}
