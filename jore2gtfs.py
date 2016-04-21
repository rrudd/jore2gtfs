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

    # Set terminal of stops in the Matinkylä cluster to Matinkylän Metro
    if stop_name == "Matinkylä (M)" or parent_station == "2000212":
        parent_station = "2000106"
    # Set terminal of stops in the Tapiola cluster to Tapiolan Metro
    if parent_station in ["2000003", "2000002"]:
        parent_station = "2000103"
    # Set terminal of stops in the Aalto cluster to Aalto University
    if stop_name in ["Tietotie", "Kemisti", "Alvar on puisto"]:
        parent_station = "2000102"
    # Set terminal of stops in the Niittykumpu cluster to Niittykumpu Metro
    if stop_name in ["Niittykumpu (M)", "Niittykumpu"]:
        parent_station = "2000105"
    # Set terminal of stops in the Urheilupuisto cluster to Urheilupuisto Metro
    if stop_id in ["E2140", "E2141"]:
        parent_station = "2000104"
    # Set terminal of stops in the Lauttasaari cluster to Lauttasaari Metro
    if stop_code in ["H1025", "H1024", "H1027"]:
        parent_station = "1000118"

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
    if stop_id not in ["2000002", "2000003", "2000212"]:
        stops.append([stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, parent_station, location_type])

with open('stops.txt', 'w') as csvfile:
    writer = csv.writer(csvfile)
    fieldnames = ['stop_id', 'stop_code', 'stop_name', 'stop_desc', 'stop_lat', 'stop_lon', 'parent_station', 'location_type']
    writer.writerow(fieldnames)
    writer.writerows(stops)
