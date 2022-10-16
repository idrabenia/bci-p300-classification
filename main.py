import os
import numpy as np
import mne
import moabb.datasets

sampling_rate = 512

dataset = moabb.datasets.bi2013a(
    NonAdaptive=True,
    Adaptive=True,
    Training=True,
    Online=True,
)

dataset.download(subject_list=[1])

data = dataset.get_data(subjects=[1])


def concat_sessions(data):
    runs_list = []
    for session_id in data.keys():
        cur_session = data[session_id]

        for run_id in cur_session:
            cur_run = cur_session[run_id]
            runs_list.append(cur_run)

    return mne.concatenate_raws(runs_list)


channels = data[1]['session_1']['run_1'].info.ch_names

for j in range(0, 24):
    raw = concat_sessions(data[j + 1])

    for i in range(0, 17):
        np.savetxt(f'./data/human{j + 1}_{channels[i]}.txt', raw[i, :][0])

    del raw
