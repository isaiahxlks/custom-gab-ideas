using System;
using System.Collections.Generic;

namespace BrrBrrCalendar
{
    public enum BrrBrrSeason
    {
        FrostSurge,
        MeltSignal,
        EchoThaw,
        ChillRitual
    }

    public class BrrBrrEvent
    {
        public string Title { get; set; }
        public DateTime Date { get; set; }
        public BrrBrrSeason Season { get; set; }
        public string Signal { get; set; }

        public override string ToString()
        {
            return $"{Date:yyyy-MM-dd} [{Season}] - {Title} :: {Signal}";
        }
    }

    public class BrrBrrCalendar
    {
        private readonly List<BrrBrrEvent> _events = new();

        public void AddEvent(string title, DateTime date, string signal)
        {
            var season = GetSeason(date);
            _events.Add(new BrrBrrEvent
            {
                Title = title,
                Date = date,
                Season = season,
                Signal = signal
            });
        }

        public List<BrrBrrEvent> GetEventsBySeason(BrrBrrSeason season)
        {
            return _events.FindAll(e => e.Season == season);
        }

        public void PrintAllEvents()
        {
            Console.WriteLine("=== BrrBrrCalendar Events ===");
            foreach (var e in _events)
            {
                Console.WriteLine(e);
            }
        }

        private BrrBrrSeason GetSeason(DateTime date)
        {
            return date.Month switch
            {
                12 or 1 or 2 => BrrBrrSeason.FrostSurge,
                3 or 4 or 5 => BrrBrrSeason.MeltSignal,
                6 or 7 or 8 => BrrBrrSeason.EchoThaw,
                9 or 10 or 11 => BrrBrrSeason.ChillRitual,
                _ => throw new ArgumentOutOfRangeException()
            };
        }
    }
}
