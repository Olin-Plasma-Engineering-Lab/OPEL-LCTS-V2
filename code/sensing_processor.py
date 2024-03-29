import serial
from time import time, ctime
from datetime import datetime


# Set time in unit seconds
t = time()

# Convert time from unit seconds to a date + time
local_time = datetime.fromtimestamp(t)

# Convert the date + time into a format that can be used in a file name
formatted_time = local_time.strftime("%Y-%m-%d_%H-%M-%S")


# Define the COM port the microcontroller is connected to
CONTROLLER_COMM_PORT = "COM5"

# Set baud rate
BAUD_RATE = 9600

# Open the COM port to start communications
serial_port = serial.Serial(CONTROLLER_COMM_PORT, BAUD_RATE, timeout=1)


with open(f"Trial {formatted_time}.csv", "w") as data:

    # Set starting time to keep track of elapsed time between measurements
    start_time = time.time()

    while True:
        sensor_output = int(serial_port.readline().decode())
        # print(sensor_output)
        # print(type(sensor_output))

        if sensor_output > 0:
            # force, temp_1, temp_2, etc = (int(sensor) for sensor in sensor_output.split(","))

            force = sensor_output
            data.write(ctime(time()))
            data.write(",")
            data.write(time.time() - start_time)
            data.write(",")
            data.write(str(force))
            data.write("\n")
