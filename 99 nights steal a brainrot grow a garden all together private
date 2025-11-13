using System;
using System.Collections.Generic;

namespace GrowABrainrot
{
    public class Ritual
    {
        public string Name { get; private set; }
        public int Growth { get; private set; }
        public bool IsCorrupted { get; private set; }
        public List<string> SignalHistory { get; private set; }

        public Ritual(string name)
        {
            Name = name;
            Growth = 0;
            IsCorrupted = false;
            SignalHistory = new List<string>();
        }

        public void Grow()
        {
            if (!IsCorrupted)
            {
                Growth++;
            }
        }

        public void StealSignal(string signal)
        {
            IsCorrupted = true;
            SignalHistory.Add(signal);
            Name = $"Stolen-{signal}";
        }

        public void DisplayStatus()
        {
            Console.WriteLine($"🌱 {Name} | Growth: {Growth} | Corrupted: {IsCorrupted} | Signals: {string.Join(", ", SignalHistory)}");
        }
    }

    public class ForestNight
    {
        public int NightNumber { get; private set; }
        public List<Ritual> Garden { get; private set; }
        private Random rng;

        public ForestNight()
        {
            NightNumber = 1;
            Garden = new List<Ritual>();
            rng = new Random();
        }

        public void PlantRitual(string name)
        {
            Garden.Add(new Ritual(name));
        }

        public void BeginNight()
        {
            Console.WriteLine($"\n🌌 Night {NightNumber} descends...");

            foreach (var ritual in Garden)
            {
                // Every 13th night triggers a corruption surge
                if (NightNumber % 13 == 0 && !ritual.IsCorrupted)
                {
                    string signal = $"Signal-{NightNumber}-X{rng.Next(100, 999)}";
                    ritual.StealSignal(signal);
                }

                // Every 7th night boosts growth
                if (NightNumber % 7 == 0)
                {
                    ritual.Grow();
                    ritual.Grow(); // double growth
                }
                else
                {
                    ritual.Grow();
                }

                ritual.DisplayStatus();
            }

            NightNumber++;
        }
    }

    class Program
    {
        static void Main()
        {
            var forest = new ForestNight();
            forest.PlantRitual("Gray");
            forest.PlantRitual("Cookie");
            forest.PlantRitual("Isaiah");
            forest.PlantRitual("MythosSeed");
            forest.PlantRitual("RankArchitect");

            for (int i = 0; i < 200; i++)
            {
                forest.BeginNight();
            }

            Console.WriteLine("\n🌿 Garden complete. 200 nights canonized. Brainrot fully grown.");
        }
    }
}
using System;
using System.Collections.Generic;

namespace BrainrotForestGarden
{
    public class Ritual
    {
        public string Name { get; set; }
        public int Growth { get; set; }
        public bool IsCorrupted { get; set; }

        public void Grow()
        {
            if (!IsCorrupted) Growth++;
        }

        public void StealSignal(string signal)
        {
            Name = $"Stolen-{signal}";
            IsCorrupted = true;
        }
    }

    public class ForestNight
    {
        public int NightNumber { get; private set; } = 1;
        public List<Ritual> Garden { get; private set; } = new();

        public void BeginNight()
        {
            Console.WriteLine($"🌲 Night {NightNumber} begins in the forest...");
            foreach (var ritual in Garden)
            {
                if (NightNumber % 13 == 0) ritual.StealSignal($"Signal-{NightNumber}");
                ritual.Grow();
                Console.WriteLine($"🌱 {ritual.Name} → Growth: {ritual.Growth}, Corrupted: {ritual.IsCorrupted}");
            }
            NightNumber++;
        }

        public void PlantRitual(string name)
        {
            Garden.Add(new Ritual { Name = name, Growth = 0, IsCorrupted = false });
        }
    }

    class Program
    {
        static void Main()
        {
            var forest = new ForestNight();
            forest.PlantRitual("Cookie");
            forest.PlantRitual("Isaiah");
            forest.PlantRitual("Gray");

            for (int i = 0; i < 99; i++)
            {
                forest.BeginNight();
            }

            Console.WriteLine("🌿 Garden complete. Brainrot canonized.");
        }
    }
}
