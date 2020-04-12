# goal: track and detect spikes in COVID outbreaks

# import modules
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import datetime as dt

# import fuctions from models.py
import models
import graph

# 1. grab data about COVID-19 statistics
content = urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv").read()
content = str(content)

# 2. process data 
complete_list = content.split("\\n")
start_date = complete_list[0].split(',')[4]
start_date = dt.datetime.strptime(start_date, "%m/%d/%y")
content_list = complete_list[1:]
infection_dict = dict()

for row in content_list:

	try:
		infections = [int(x) for x in row.split(',')[4:]]
		location = row.split(',')[1]+'-'+row.split(',')[0]
		infection_dict[location] = infections

	# temporary fix for unused data (should be)
	except ValueError:
		pass
	except IndexError:
		pass

list_of_keys = list(infection_dict.keys())

# 3. detect spikes
y_values = []
labels = []

for key in list_of_keys:
	# TODO: Modify country name
	if "canada" in key.lower():
		y_values.append(infection_dict[key])
		labels.append(key)

# graph Canada data and save file as cases.png
graph.graph_cases(start_date, y_values, labels, "cases.png")

# Bonus: prediction 

# TODO: Modify province name
province_name = "Quebec"

# defining data
X_data = np.array(list(range(len(infection_dict["Canada-"+province_name]))))
y_data = np.array(infection_dict["Canada-"+province_name])		# total infections
y_data_deriv = models.derive_data(y_data)						# daily infections

# find parameters
a, k, x0 = models.calculate_parameters(X_data[:len(y_data_deriv)], y_data_deriv)

# generate predictions

# TODO: modify prediction range
n_days = 30

predicted_total_infections = [models.sigmoid(x, a, k, x0) for x in range(len(X_data)+n_days)] 
predicted_daily_infections = [models.sigmoid_deriv(x, a, k, x0) for x in range(len(X_data[:-1])+n_days)]

# graph predictions and save file as predictions.png
graph.graph_predictions(start_date, y_data, predicted_total_infections, y_data_deriv, predicted_daily_infections, location=province_name, filename="predictions.png")
