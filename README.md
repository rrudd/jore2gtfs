# jore2gtfs

Jore2gtfs is a simple python script that converts stop information from HSL Joukkoliikennerekisteri to a GTFS formatted CSV for use e.g. with OpenTripPlanner.

## Usage

You can find data dumps from jore [here](http://dev.hsl.fi/infopoiminta/). Place the `pysakki.dat` and `terminaali.dat` files in the same folder as `jore2gtfs.py`. Run the script and it will produce a properly formatted `stops.txt`.
