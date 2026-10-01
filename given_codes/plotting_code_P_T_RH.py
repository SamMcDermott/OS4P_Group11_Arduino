"Plotting code for the P T RH output"

import csv
import matplotlib.pyplot as plt

# Read the data from the CSV file
time_s = []
temp = []
pressure = []
humidity = []

with open("data.csv") as f: #Replace data.csv whit relevant data file
    reader = csv.DictReader(f)
    for row in reader:
        time_s.append(float(row["Time (seconds)"]))
        temp.append(float(row["Temperature (C)"]))
        pressure.append(float(row["Pressure (Pa)"]))
        humidity.append(float(row["Humidity (%)"]))

# Plot the data in seperate figures

# Pressure
plt.figure()
plt.plot(time_s, pressure, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (Pa)")
plt.grid(True)

plt.savefig("pressure_plot.png")
plt.close()

# Temperature
plt.figure()
plt.plot(time_s, temp, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.grid(True)

plt.savefig("Temperature_plot.png")
plt.close()

# Humidity
plt.figure()
plt.plot(time_s, humidity, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.grid(True)

plt.savefig("Humidity_plot.png")
plt.close()

