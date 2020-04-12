import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def graph_cases(start_date, y_values, labels, filename):
	now = start_date
	then = now + dt.timedelta(days=len(y_values[0]))
	days = mdates.drange(now,then,dt.timedelta(days=1))

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))

	for i in range(len(y_values)):
		plt.plot(days, y_values[i], label=labels[i])

	plt.legend(loc="upper left")
	plt.gcf().autofmt_xdate()

	plt.savefig(filename)

def graph_predictions(start_date, total_infections, predicted_total_infections, daily_infections, predicted_daily_infections, location, filename):
	now = start_date
	then = now + dt.timedelta(days=len(predicted_total_infections))
	days = mdates.drange(now,then,dt.timedelta(days=1))

	plt.subplot(2,1,1)
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=12))
	plt.title("New COVID-19 Infections in "+location)
	plt.plot(days[1:len(predicted_total_infections)], predicted_daily_infections, label="Predicted", linestyle="--")
	plt.plot(days[1:len(daily_infections)+1], daily_infections, label="Observed")
	plt.xlabel("Date")
	plt.ylabel("New infections per day")
	plt.legend()
	plt.grid()
	plt.gcf().autofmt_xdate()


	plt.subplot(2,1,2)
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=12))
	plt.title("Total COVID-19 Infections in "+location)
	plt.plot(days[:len(predicted_total_infections)], predicted_total_infections, label="Predicted", linestyle="--")
	plt.plot(days[:len(total_infections)], total_infections, label="Observed")
	plt.xlabel("Date")
	plt.ylabel("Cumulative infections")
	plt.legend()
	plt.grid()


	plt.subplots_adjust(hspace=.7)
	plt.gcf().autofmt_xdate()
	plt.savefig(filename)
