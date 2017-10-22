public struct Location {
    double lat, lon;

    public Location(double lat, double lon) {
        this.lon = lon;
        this.lat = lat;
    }

    public double Latitude {
        get { return this.lat; }
    }

    public double Longtitude {
        get { return this.lon; }
    }
}