using System;

namespace Tarea_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Escribe tu edad: ");
            int age = Convert.ToInt32(Console.ReadLine());

            if(age > 100)
            {
                Console.WriteLine("Esa edad ya esta murida papu :v");
            }
            else
            {
                GetEdades(age);
            }
        }

        static void GetEdades(int currentAge)
        {
            for(int age = 1; age<= 100; age++)
            {
                if(age == currentAge)
                {
                    Console.WriteLine("Tienes " + age + " años");
                    break;
                }
                Console.WriteLine(age);
            }
        }
    }
}
