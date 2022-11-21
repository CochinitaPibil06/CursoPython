using System;

namespace Tarae_4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
            Console.Write("Escribe un numero de la semana: ");
            int dia =  Convert.ToInt32(Console.ReadLine());
            DiaSemana(dia);
            //string valor = "Hola";
            //string valor = "mundo";
            //string valor = "";

            //switch (valor)
            //{
            //    case "Hola":
            //        Console.WriteLine(valor + " mundo");

            //        break;

            //    case "mundo":
            //        Console.WriteLine("Hola " + valor);

            //        break;

            //    default:
            //        Console.WriteLine("Hola mundo :)");
            //        break;
            //}


            static void DiaSemana(int Dia)
            {
                switch (Dia)
                {
                    case 1:
                        Console.WriteLine("lunes");
                        break;

                    case 2:
                        Console.WriteLine("marte");
                        break;

                    case 3:
                        Console.WriteLine("miercole");
                        break;

                    case 4:
                        Console.WriteLine("jueves");
                        break;

                    case 5:
                        Console.WriteLine("viernes");
                        break;

                    case 6:
                        Console.WriteLine("sabado");
                        break;

                    case 7:
                        Console.WriteLine("domingo");
                        break;

                    default:
                        Console.WriteLine("Ese dia no existe");
                        break;
                }
            }

        }
    }
}
