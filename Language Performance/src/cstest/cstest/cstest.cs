using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Threading;

namespace cstest
{
    public class cstest
    {
        public static void Main(string[] args)
        {
            var stopwatch = new Stopwatch();
            stopwatch.Start();

            int i = 0;

            while (i != 1000000000)
            {
                i++;
            }

            stopwatch.Stop();
            Console.WriteLine($"Time taken by C#: {stopwatch.ElapsedMilliseconds / 1000.0} secs");

            Thread.Sleep(1000);
        }
    }
}
