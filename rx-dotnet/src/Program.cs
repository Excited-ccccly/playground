using System;

namespace rx_dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            LocationTracker provider = new LocationTracker();
            LocationReporter reporter1 = new LocationReporter("FixedGPS");
            reporter1.Subscribe(provider);
            LocationReporter reporter2 = new LocationReporter("MobileGPS");
            reporter2.Subscribe(provider);

            provider.TrackLocation(new Location(1, 2));
            reporter1.Unsubscribe();
            provider.TrackLocation(new Location(3, 4));
            provider.TrackLocation(null);
            provider.EndTransmission();
        }
    }
}
