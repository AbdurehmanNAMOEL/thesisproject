import numpy as np
import matplotlib.pyplot as plt


def messag_signal(am, fm):
    Am = am
    Fm = fm
    fs = 2000
    t = np.arange(0, 0.5, 1 / fs)
    Message_signal = Am *np.sin(2*np.pi*Fm*t)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("Message Signal")
    plt.plot(t, Message_signal)
    plt.savefig('graph22.png')


def carrier_signal(cm, fc):
    Cm = cm
    Fc = fc
    fs = 2000
    t = np.arange(0, 0.5, 1/fs)
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


def am_modulated_signal(am, fm, cm, fc):
    Cm = cm
    Fc = fc
    Am = am
    Fm = fm
    fs = 2000
    t = np.arange(0, 0.5, 1/fs)
    Message_signal = Am * np.cos(2 * np.pi * Fm * t)
    Carrier_signal = Cm*np.cos(2*np.pi*Fc*t)
    Modulated_signal = Carrier_signal + (Message_signal*np.cos(2*np.pi*Fc*t))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("Modulated Signal")
    plt.plot(t, Modulated_signal)
    plt.savefig('graph44.png')

def demodulated_signal(am, fm, cm, fc):
    Cm = cm
    Fc = fc
    Am = am
    Fm = fm
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    Message_signal = Am * np.cos(2 * np.pi * Fm * t)
    Carrier_signal = Cm * np.cos(2 * np.pi * Fc * t)
    Modulated_signal = Carrier_signal + (Message_signal * np.cos(2 * np.pi * Fc * t))
    DEModulated_signal = Modulated_signal*(2*np.cos(2*np.pi*fc*t))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor("#b2b5a3")
    ax.patch.set(facecolor="#41a8aa")
    plt.xlabel("                                           time(s)")
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.title("Demodulated Signal")
    plt.plot(t, DEModulated_signal)
    plt.savefig('graph55.png')



