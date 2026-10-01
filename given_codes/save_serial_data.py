"""
Code to save data from the sd card to a local file 

NOTE that the arduino needs to be connected to your leptop and no other programs should be useing
the the usbc port, i.e. close anny arduino IDE programs on your laptop

NOTE that the given direction in line - port = sys.argv[1] if len(sys.argv) > 1 else "/dev/cu.usbmodem101" - should be changed
to the right port, see below for more details
"""

import sys
import time
import serial

# Change the next line to match your Arduino's port.
# You can find it in the Arduino IDE under Tools > Port.
# Examples: "COM3" on Windows, "/dev/ttyACM0" or "/dev/ttyUSB0" on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else "/dev/cu.usbmodem101"
baud_rate = 9600
out_file = "data.csv"

# Opening the serial port resets the Arduino, which runs
# extract_data_from_csv.ino from the start and sends the file contents.
ser = serial.Serial(port, baud_rate, timeout=2)
time.sleep(2)  # give the Arduino time to reset and start sending

with open(out_file, "w", newline="") as f:
    while True:
        line = ser.readline()
        if not line:
            break  # no more data for 2 seconds, assume it's done
        f.write(line.decode())

ser.close()
print(f"Saved data to {out_file}")
