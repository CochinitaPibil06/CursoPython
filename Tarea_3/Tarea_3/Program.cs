using System;

namespace Tarea_3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool ciclo = true;

            while (ciclo)
            {
                Console.Write("Escribe algo: ");
                string valor = Console.ReadLine();

                if (salir(valor))
                {
                    ciclo = false;
                }
                else
                {
                    Console.WriteLine(valor);
                }
            }

            Console.WriteLine("fin del codigo");
        }

        static bool salir(string valor)
        {
            bool validacion = false;

            if (valor == "salir")
                validacion = true;

            return validacion;
        }
    }
}
