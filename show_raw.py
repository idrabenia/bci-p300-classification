import os
import numpy as np
import mne
import moabb.datasets
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

sampling_rate = 512

dataset = moabb.datasets.bi2013a(
    NonAdaptive=True,
    Adaptive=True,
    Training=True,
    Online=True,
)

dataset.download(subject_list=[1])

data = dataset.get_data(subjects=[1])

raw = data[1]['session_1']['run_1']

raw.filter(l_freq=4, h_freq=None)

# raw.plot_psd(fmax=30)

raw.plot(duration=1, n_channels=5, start=10)

plt.show()
