import numpy as np
import matplotlib.pyplot as plt

from FM_DEModulation_TEST import *
def messag_signal(am, fm):
    Am = am
    Fm = fm
    fs = 2000
    x = np.arange(0, 0.5, 1/fs)
    Message_signal = Am *np.cos(2*np.pi*Fm*x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("Message Signal")
    plt.plot(x, Message_signal)
    plt.savefig('graph22.png')



def carrier_signal(cm, fc):
    Cm = cm
    Fc = fc
    fs = 2000
    t = np.arange(0, 0.2, 1/fs)
    Carrier_signal = Cm *np.cos(2*np.pi*Fc*t)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("carrier Signal")
    plt.plot(t, Carrier_signal)
    plt.savefig('graph33.png')


def fm_modulated_signal(am, fm, cm, fc):
    Ac = cm
    Fc = fc
    Am = am
    Fm = fm
    # modulator sensetivity
    kf =0.5
    fs = 10*Fc
    t = np.arange(0, 0.5, 1/fs)
    # Message_signal = Am*np.sin(2 * np.pi * Fm * t)
    Fm_Modulated_signal =Ac*np.cos((2 * np.pi * Fc * t) + (2*np.pi*kf*np.sin(2*np.pi*Fm*t)))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("Frequency_Modulated Signal")
    plt.plot(t, Fm_Modulated_signal)
    plt.savefig('graph66.png')
#
#
#
# sampling_freq = 44100
# T = 1 / sampling_freq
# fm = 4
# fc = 3150
# kf = 10
# ts = np.arange(0, 1 - T, T)
# ts2 = np.arange(0, 44098)
# xm = np.sin(2*np.pi*fm*ts) # Modulating signal
# kf= 10 # Modulation factor

# def fm_demodulated_signal():
#     sampling_freq = 44100
#     T = 1 / sampling_freq
#     fm = 4
#     fc = 3150
#     kf = 10
#     ts = np.arange(0, 1 - T, T)
#     ts2 = np.arange(0, 44098)
#     xm = np.sin(2 * np.pi * fm * ts)  # Modulating signal
#     kf = 10  # Modulation factor
#     # Message_signal = Am*np.sin(2 * np.pi * Fm * t)
#     Fm_Modulated_signal = 10 * np.cos((2 * np.pi * fc * ts) + 2 * np.pi * kf * np.sin(2 * np.pi * fm * ts))
#     xd = fm_demod(Fm_Modulated_signal, 10, fc)
#     Message_signal = Am*np.sin(2 * np.pi * Fm * t)
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     fig.patch.set_facecolor("#b2b5a3")
#     ax.patch.set(facecolor="#41a8aa")
#     plt.xlabel("                                           time(s)")
#     plt.grid(True)
#     plt.ylabel("Amplitude")
#     plt.title("Frequency_Modulated Signal")
#     plt.plot(ts2, xd)
#     plt.savefig('graph88.png')
