import pickle
import matplotlib.pyplot as plt
import numpy as np

fname = 'pickle/2026-06-14-144203.pickle'
#fname = 'pickle/2026-06-17-202140_2km.pickle'


# DabrowskiBuschStelzer-Radar.pdf:
angle_increment = 2.0*np.pi/4096.0

# status: 02 valid data
# scale: meters = scale * 10/sqrt(2)

# Open file in read-binary mode
with open(fname, 'rb') as file:
    # Load the pickled data
    data = pickle.load(file)

#print('Retrieved pickled data:')
#for i, item in enumerate(data):
#    print(f'Data {i}: {item}')

n_scanlines = 2048
n_rg = 512

print('scale', data[0]['scale'], hex(data[0]['scale']))
r_max = data[0]['scale'] * 10/np.sqrt(2) # meters
print(f'{r_max=}')
r = np.linspace(0, r_max, n_rg)
theta = np.linspace(0, 2*np.pi, n_scanlines)
scandata = np.empty((n_scanlines, n_rg), dtype=np.uint8)

for i, item in enumerate(data):
    scandata[i, :] = np.frombuffer(item['data'], dtype=np.uint8)

fig, ax = plt.subplots(figsize=(10, 4))
extent = (0, 360, np.min(r), np.max(r))
im = ax.imshow(scandata.T, interpolation='none', aspect='auto', origin='lower', extent=extent)
ax.set_xlabel('Azimuth / °')
ax.set_ylabel('Range / m')
fig.colorbar(im)
fig.tight_layout()

plt.show()