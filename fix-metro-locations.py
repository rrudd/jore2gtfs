from tempfile import NamedTemporaryFile
import shutil
import csv

fileName = 'stops.txt'
tempFile = NamedTemporaryFile(mode='w', delete=False)

with open(fileName) as csvFile, tempFile:
    reader = csv.reader(csvFile, delimiter=',')
    writer = csv.writer(tempFile, delimiter=',')

    for row in reader:
        # Tapiola
        if row[0] in ['2211601', '2211602']:
            row[4] = '60.175449'
            row[5] = '24.802475'

        # Urheilupuisto
        if row[0] in ['2214601', '2214602']:
            row[4] = '60.174708'
            row[5] = '24.779596'

        # Niittykumpu
        if row[0] in ['2214603', '2214604']:
            row[4] = '60.17047'
            row[5] = '24.76275'

        # Keilaniemi
        if row[0] in ['2222601', '2222602']:
            row[4] = '60.174951'
            row[5] = '24.828714'

        # Aalto
        if row[0] in ['2222603', '2222604']:
            row[4] = '60.184746'
            row[5] = '24.825647'

        # Matinkylä
        if row[0] in ['2314601', '2314602']:
            row[4] = '60.160050'
            row[5] = '24.739981'

        writer.writerow(row)

shutil.move(tempFile.name, fileName)
