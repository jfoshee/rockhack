import las
import json
import requests
import os
import fnmatch

url = 'http://fuzzylas.appspot.com/lookup?'

input_dir = '../geohack_well_data'
output_dir = 'well_info'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for path, dirs, files in os.walk(input_dir):

    for f in fnmatch.filter(files, '*.las'):
        las_file = os.path.join(path, f)
        las_reader = las.LASReader(las_file)

        output_file = os.path.join(output_dir,f.split('.')[0]) +".txt"
        

        with open(output_file, 'w') as output:
            for name in las_reader.data.dtype.names:

                r = requests.get(url + 'mnemonic=%s&guesses=1&format=json'
                                 %name)
                if name in r.json()[0]:
                    output.write(name + ','
                                 + r.json()[0][name][0]['description'] + '\n')
