import las
import json

las_file = 'NEWBURN_1.las'
las_reader = las.LASReader(las_file)

output_file = 'www/log_json.json'
data = las_reader.data

las_dict = {}
for name in data.dtype.names:
    las_dict[name] = data[name].tolist()

json_out = json.dumps(las_dict)

with open(output_file, 'w') as outfile:

    outfile.write('var logData =' + json_out +';')



