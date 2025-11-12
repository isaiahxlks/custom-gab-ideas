using System;
using System.Collections.Generic;

public class Island
{
    public string Name { get; set; }
    public bool IsInhabited { get; set; }
    public List<string> Wildlife { get; set; }

    public Island(string name, bool isInhabited)
    {
        Name = name;
        IsInhabited = isInhabited;
        Wildlife = new List<string>();
    }

    public void AddWildlife(string creature)
    {
        Wildlife.Add(creature);
        Console.WriteLine($"🦎 {creature} added to {Name}");
    }

    public void Describe()
    {
        Console.WriteLine($"\n🏝️ {Name} — {(IsInhabited ? "Inhabited" : "Uninhabited")}");
        Console.WriteLine("Wildlife:");
        foreach (var animal in Wildlife)
        {
            Console.WriteLine($"- {animal}");
        }
    }
}

public class Archipelago
{
    public string Title { get; set; }
    public List<Island> Islands { get; set; }

    public Archipelago(string title)
    {
        Title = title;
        Islands = new List<Island>();
    }

    public void AddIsland(Island island)
    {
        Islands.Add(island);
        Console.WriteLine($"🌊 Island '{island.Name}' added to {Title}");
    }

    public void PopulateWildlife(List<string> creatures)
    {
        var rand = new Random();
        foreach (var island in Islands)
        {
            int count = rand.Next(1, creatures.Count);
            for (int i = 0; i < count; i++)
            {
                string creature = creatures[rand.Next(creatures.Count)];
                island.AddWildlife(creature);
            }
        }
    }

    public void DescribeAll()
    {
        Console.WriteLine($"\n🌐 Archipelago: {Title}");
        foreach (var island in Islands)
        {
            island.Describe();
        }
    }
}
