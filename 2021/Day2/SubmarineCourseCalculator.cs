using System;
using System.Collections.Generic;
using System.Linq;

namespace Day2
{
    public static class SubmarineCourseCalculator
    {
        public static int Part1()
        {
            var data = GetData();
            var up = data.Where(directions => directions.ToLower().Contains("up")).Select(s => int.Parse(s.Last().ToString())).Sum();
            var down = data.Where(directions => directions.ToLower().Contains("down")).Select(s => int.Parse(s.Last().ToString())).Sum();
            var forward = data.Where(directions => directions.ToLower().Contains("forward")).Select(s => int.Parse(s.Last().ToString())).Sum();

            var result = down - up;
            var t = result * forward;

            return t;
        }

        private static List<string> GetData()
        {
            const string dataPath = @"C:\Users\CHRISTOPHER252\source\repos\adventofcode\2021\Day2\SubmarineCourse.txt";

            var data = System.IO.File.ReadLines(dataPath)
                .ToList();

            return data;
        }
    }
}
