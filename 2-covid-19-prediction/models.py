import numpy as np
from scipy.optimize import curve_fit

def sigmoid(x, a, k, x0):
	return a/(1 + np.exp(-k * (x - x0)))

def sigmoid_deriv(x, a, k, x0):
	return (a*k*np.exp(-k * (x - x0)))/((1+np.exp(-k * (x - x0)))**2)

def derive_data(data):
	N = len(data) - 1
	return_list = []
	for i in range(N):
		return_list.append(data[i+1]-data[i])
	return return_list

def calculate_parameters(X_data, y_data, a_guess=2e4, k_guess=1, x0_guess=70):
	parameters, covariance = curve_fit(sigmoid_deriv, X_data, y_data, [a_guess, k_guess, x0_guess])
	return parameters
