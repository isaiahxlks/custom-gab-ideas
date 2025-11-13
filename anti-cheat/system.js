// antiCheat.cs — branded integrity for Grow a Brainrot
using System;
using System.Collections.Generic;

namespace GrowABrainrot
{
    public static class AntiCheat
    {
        private static readonly HashSet<string> flaggedSignals = new()
        {
            "inject.rank",
            "spoof.trigger",
            "bypass.lore",
            "forge.ascension"
        };

        public static bool Validate(string ritual)
        {
            if (flaggedSignals.Contains(ritual))
            {
                Console.WriteLine($"[🚫] AntiCheat triggered: {ritual} is forbidden.");
                return false;
            }

            Console.WriteLine($"[✅] Ritual passed: {ritual} is clean.");
            return true;
        }
    }

    public class SecureSignal
    {
        public static void Emit(string ritual)
        {
            if (AntiCheat.Validate(ritual))
            {
                Signal.Emit(ritual); // from brainrot.cs
            }
            else
            {
                Console.WriteLine("[🧱] Ritual blocked. No ascension.");
            }
        }
    }
}

