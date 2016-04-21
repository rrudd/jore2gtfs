import io
import csv

stops = []

for line in io.open('pysakki.dat', encoding='ISO_8859-1'):
    stop_id = line[1:8]
    stop_code = line[177:183].replace(" ", "")
    stop_name = line[38:58].strip()
    stop_desc = line[78:98].strip()
    stop_lat = line[22:30]
    stop_lon = line[30:38]
    parent_station = line[219:226].strip()
    location_type = 0
    stops.append([stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, parent_station, location_type])

for line in io.open('terminaali.dat', encoding='ISO_8859-1'):
    stop_id = line[1:8]
    stop_code = ''
    stop_name = line[8:48].strip()
    stop_desc = ''
    stop_lat = line[102:110]
    stop_lon = line[110:118]
    parent_station = ''
    location_type = 1
    stops.append([stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, parent_station, location_type])

with open('stops.txt', 'w') as csvfile:
    writer = csv.writer(csvfile)
    fieldnames = ['stop_id', 'stop_code', 'stop_name', 'stop_desc', 'stop_lat', 'stop_lon', 'parent_station', 'location_type']
    writer.writerow(fieldnames)
    writer.writerows(stops)
