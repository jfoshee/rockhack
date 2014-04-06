from agilegeo.wavelet import ricker
import numpy as np
import json

outfile = 'www/seismic.seis'

dt = .001

f1 = 15.0
f2 = 150.0

wavelet = ricker(0.2,dt, 25)

reflect = np.random.randn(1000)

seis = np.convolve(wavelet, reflect, mode='same')

z = np.linspace(1000, 6000, seis.size)

j_dict = {'z':z.tolist(), 'seis':seis.tolist()}
j_out = json.dumps(j_dict)

with open(outfile, 'w') as output:
    output.write('var seisData =' + j_out +';')





