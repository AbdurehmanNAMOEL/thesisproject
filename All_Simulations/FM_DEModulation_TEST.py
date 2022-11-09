import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

sampling_freq = 44100
T = 1/sampling_freq
fm = 4
fc = 3150
ts = np.arange(0,1-T,T)
ts2 = np.arange(0,44098)
xm = np.sin(2*np.pi*fm*ts) # Modulating signal
kf= 10 # Modulation factor
# xc = 10*np.sin(2*np.pi*fc*ts+(mf*xm)) #Modulated carrier
xc = 10 * np.cos((2 * np.pi * fc * ts) + (2 * np.pi * kf) * np.sin(2 * np.pi * fm * ts))

def fm_demod(x, df=1.0, fc=0.0):

    # Making complex signal from real values input
    z = hilbert(x)

    # Remove carrier.
    n = np.arange(0, len(z))
    rx = z*np.exp(-1j*2*np.pi*fc*n)

    # Extract phase of carrier.
    phi = np.arctan2(np.imag(rx), np.real(rx))

    # Calculate frequency from phase.
    y = np.diff(np.unwrap(phi)/(2*np.pi*df))

    return y


xd = fm_demod(xc, 10, fc) # Demodulated signal
data = np.fft.rfft(xd) # Demodulated signal spectrum
fig, (ax3) = plt.subplots(1, 1)
ax3.plot(ts2, xd)
ax3.set_title('Demodulated signal')
plt.savefig('graph88.png')