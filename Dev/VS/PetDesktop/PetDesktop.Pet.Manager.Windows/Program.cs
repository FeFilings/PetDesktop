using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;

namespace PetDesktop.Pet.Manager.Windows
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        static void Main()
        {
            ServiceBase[] ServicesToRun;
            ServicesToRun = new ServiceBase[]
            {
                new PetManager()
            };
            ServiceBase.Run(ServicesToRun);
        }

        public static int GetPetCount()
        {
            // Lets get the number of pets in a file on the desktop
            string desktopPath = @"C:\Users\roger\Desktop\pets.txt";
            if (System.IO.File.Exists(desktopPath))
            {
                string[] lines = System.IO.File.ReadAllLines(desktopPath);
                if (lines.Length > 0)
                {
                    if (int.TryParse(lines[0], out int petCount))
                    {
                        return petCount;
                    }
                }
            }
            else
            {
                System.IO.File.WriteAllText(desktopPath, "0");
                return 0;
            }
        }
    }
}
