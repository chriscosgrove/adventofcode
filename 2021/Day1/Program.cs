using System;

namespace Day1
{
    class Program
    {
        static void Main(string[] args)
        {
            var increasedDepths = SonarDepthCalculator.Part1();
            Console.WriteLine($"Increased Depths: {increasedDepths}");
            Console.ReadKey();
        }
    }
}
