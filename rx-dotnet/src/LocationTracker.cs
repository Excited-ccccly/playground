using System;
using System.Collections.Generic;

public class LocationTracker : IObservable<Location>
{
    private List<IObserver<Location>> observers;

    public LocationTracker()
    {
        this.observers = new List<IObserver<Location>>();
    }

    public List<IObserver<Location>> Observers { get => observers; set => observers = value; }

    IDisposable IObservable<Location>.Subscribe(IObserver<Location> observer)
    {
        if (!observers.Contains(observer))
        {
            observers.Add(observer);
        }
        return new Unsubscriber(observers, observer);
    }

    public void TrackLocation(Nullable<Location> loc)
    {
        foreach (var observer in observers)
        {
            if (!loc.HasValue)
            {
                observer.OnError(new Exception());
            }
            else
            {
                observer.OnNext(loc.Value);
            }
        }
    }

    public void EndTransmission()
    {
        foreach (var observer in observers)
        {
            if (observers.Contains(observer))
            {
                observer.OnCompleted();
            }
        }
        observers.Clear();

    }
}

internal class Unsubscriber : IDisposable
{
    private List<IObserver<Location>> observers;
    private IObserver<Location> observer;

    public Unsubscriber(List<IObserver<Location>> observers, IObserver<Location> observer)
    {
        this.observers = observers;
        this.observer = observer;
    }

    void IDisposable.Dispose()
    {
        if (observer != null && observers.Contains(observer))
        {
            observers.Remove(observer);
        }
    }
}