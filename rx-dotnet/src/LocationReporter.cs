
using System;

public class LocationReporter : IObserver<Location>
{
    private IDisposable unsubscriber;
    private string instName;

    public string Name {
        get { return this.instName; }
    }

    public virtual void Subscribe(IObservable<Location> provider) {
        if (provider != null) {
            unsubscriber = provider.Subscribe(this);
        }
    }
    public LocationReporter(string name) => this.instName = name;

    public virtual void Unsubscribe() {
        this.unsubscriber.Dispose();
    }

    public void OnCompleted()
    {
        Console.WriteLine("mission complete");
        this.Unsubscribe();
    }

    public void OnError(Exception error)
    {
        Console.WriteLine("Location can not be determined");
    }

    public void OnNext(Location value)
    {
        Console.WriteLine("{2}: Current location is {0}, {1}", value.Latitude, value.Longtitude, this.Name);
    }
}