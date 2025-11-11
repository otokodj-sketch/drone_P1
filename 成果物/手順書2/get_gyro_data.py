import serial
import matplotlib.pyplot as plt
import time
from collections import deque

PORT = 'COM5'   # ←自分の環境に合わせて変更
BAUD = 115200
WINDOW_SIZE = 100

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

gx_data = deque(maxlen=WINDOW_SIZE)
gy_data = deque(maxlen=WINDOW_SIZE)
gz_data = deque(maxlen=WINDOW_SIZE)

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot([], [], label="Gyro X")
line2, = ax.plot([], [], label="Gyro Y")
line3, = ax.plot([], [], label="Gyro Z")
ax.legend()
ax.set_ylim(-500, 500)
ax.set_xlim(0, WINDOW_SIZE)

while True:
    line = ser.readline().decode('utf-8').strip()
    if not line:
        continue

    try:
        gx, gy, gz = map(float, line.split(','))
        gx_data.append(gx)
        gy_data.append(gy)
        gz_data.append(gz)

        line1.set_data(range(len(gx_data)), gx_data)
        line2.set_data(range(len(gy_data)), gy_data)
        line3.set_data(range(len(gz_data)), gz_data)
        ax.relim()
        ax.autoscale_view()
        plt.pause(0.01)

    except ValueError:
        pass
