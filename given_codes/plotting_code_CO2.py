import csv
import matplotlib.pyplot as plt

# Read the data from the CSV file
time_s = []
co2 = []

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        time_s.append(float(row["Time (seconds)"]))
        co2.append(float(row["CO2 (ppm)"]))

# Plot the data
plt.plot(time_s, co2, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("CO2 (ppm)")
plt.grid(True)

plt.savefig("CO2_plot.png")
plt.show()
