using System;

namespace Tarea_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool ciclo = true;
            while (ciclo) 
            {
                pintarMenu();

                int opcion = Convert.ToInt32(Console.ReadLine());
                int num1 = 0, num2 = 0;

                switch (opcion)
                {
                    case 1:
                        Console.Write("Numero 1: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        Console.Write("Numero 2: ");
                        num2 = Convert.ToInt32(Console.ReadLine());
                        suma(num1, num2);
                        break;

                    case 2:
                        Console.Write("Numero 1: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        Console.Write("Numero 2: ");
                        num2 = Convert.ToInt32(Console.ReadLine());
                        resta(num1, num2);
                        break;

                    case 3:
                        Console.Write("Numero 1: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        Console.Write("Numero 2: ");
                        num2 = Convert.ToInt32(Console.ReadLine());
                        multiplicacion(num1, num2);
                        break;

                    case 4:
                        Console.Write("Numero 1: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        Console.Write("Numero 2: ");
                        num2 = Convert.ToInt32(Console.ReadLine());
                        divicion(num1, num2);
                        break;

                    case 5:
                        Console.Write("Numero: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        alcuadrado(num1);
                        break;

                    case 6:
                        Console.Write("Numero: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        alcubo(num1);
                        break;

                    case 7:
                        Console.Write("Numero 1: ");
                        num1 = Convert.ToInt32(Console.ReadLine());
                        Console.Write("Numero 2: ");
                        num2 = Convert.ToInt32(Console.ReadLine());
                        residuo(num1, num2);
                        break;

                    case 8:
                        ciclo = false;
                        break;

                    default:
                        Console.WriteLine("esa opcion no existe");
                        break;
                }
            }

            Console.WriteLine("Fin");
        }

        static void pintarMenu()
        {
            Console.WriteLine("------ Menu ------");
            Console.WriteLine("1) Sumar");
            Console.WriteLine("2) Restar");
            Console.WriteLine("3) Multiplicar");
            Console.WriteLine("4) Dividir");
            Console.WriteLine("5) Elevar al cuadrado");
            Console.WriteLine("6) Elevar al cubo");
            Console.WriteLine("7) Residuo");
            Console.WriteLine("8) Salir");
            Console.WriteLine("--------------------");
            Console.WriteLine("Pon el numero de la opcion que desea ejecutar: ");
        }

        static void resta(int num1, int num2)
        {
            Console.WriteLine(num1 - num2);
        }

        static void multiplicacion(int num1, int num2)
        {
            Console.WriteLine(num1 * num2);
        }

        static void suma(int num1, int num2)
        {
            Console.WriteLine(num1 + num2);
        }

        static void divicion(int num1, int num2)
        {
            Console.WriteLine(num1 / num2);
        }

        static void alcuadrado(int num1)
        {
            Console.WriteLine(Math.Pow(num1, 2));
        }

        static void alcubo(int num1)
        {
            Console.WriteLine(Math.Pow(num1, 3));
        }

        static void residuo(int num1, int num2)
        {
            Console.WriteLine(num1 % num2);
        }
    }
}
