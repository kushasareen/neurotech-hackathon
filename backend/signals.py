from standard_CCA import standard_cca
import numpy as np
from scipy.signal import filtfilt, cheby1, iirnotch


def get_relaxation(bci_data, freq_range = [8,13], n_levels = 5):
	prediction = None
	corr = []
	sampling_rate = 250.0
	low_bound_freq = freq_range[0] - 0.25
	upper_bound_freq = freq_range[1] + 0.25
	channels = [0]
	num_harmonics = 1
	nyq_freq = sampling_rate / 2


	freq_levels = np.linspace(freq_range[0], freq_range[1], n_levels)
	bci_data -= np.nanmean(bci_data, axis=0)

	beta, alpha = cheby1(N=2, rp=0.3, Wn=[low_bound_freq / nyq_freq, upper_bound_freq / nyq_freq], btype='band', output='ba')
	bci_data = filtfilt(beta, alpha, bci_data.T).T

	for frequency in freq_levels:
	    rho, _, _, _ = standard_cca(bci_data[:, channels], sampling_rate, float(frequency), num_harmonics)
	    corr.append(rho)

	prediction_index = np.argmax(corr)
	print(freq_levels[prediction_index])

	return prediction_index

	

if __name__ == "__main__":
	print(get_relaxation(np.random.randn(1000, 8)))
	
