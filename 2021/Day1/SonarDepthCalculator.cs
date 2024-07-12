using System;
using System.Collections.Generic;
using System.Linq;

namespace Day1
{
    public static class SonarDepthCalculator
    {
        public static int Part1()
        {
            const string dataPath = @"C:\Users\CHRISTOPHER252\source\repos\adventofcode\2021\Day1\SonarDepthData.txt";

            var data = System.IO.File.ReadLines(dataPath)
                .Select(int.Parse)
                .ToList();

            var counter = 0;
            var previous = -1;

            data.ForEach(current =>
            {
                if (previous != -1 && current > previous)
                {
                    counter++;
                }

                previous = current;
            });

            return counter;
        }
    }
}
