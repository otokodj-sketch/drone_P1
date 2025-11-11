import serial
import matplotlib.pyplot as plt
from collections import deque
import time

PORT = "COM3"    # ← Arduino IDEで確認したポートに変更
BAUD = 115200

def main():
    ser = serial.Serial(PORT, BAUD, timeout=1)
    N = 200
    values = deque([0]*N, maxlen=N)
    times  = deque([0]*N, maxlen=N)
    start_time = time.time()

    plt.ion()
    fig, ax = plt.subplots()
    line_data, = ax.plot(list(times), list(values), label="light")
    min_line = ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, label='min')
    max_line = ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, label='max')
    text_current = ax.text(0.02, 0.95, "current: ---", transform=ax.transAxes, fontsize=12, verticalalignment='top')

    ax.set_xlabel("time [s]")
    ax.set_ylabel("light sensor (ADC)")
    ax.set_title("Light sensor live")
    ax.legend(loc="lower right")

    try:
        while True:
            raw = ser.readline().decode(errors="ignore").strip()
            if raw.isdigit():
                v = int(raw)
                t = time.time() - start_time
                values.append(v)
                times.append(t)
                line_data.set_xdata(list(times))
                line_data.set_ydata(list(values))
                vmin = min(values)
                vmax = max(values)
                margin = max(20, (vmax - vmin) * 0.2)
                ax.set_ylim(vmin - margin, vmax + margin)
                ax.set_xlim(times[0], times[-1])
                min_line.set_ydata([vmin, vmin])
                max_line.set_ydata([vmax, vmax])
                text_current.set_text(f"current: {v}\nmin: {vmin}\nmax: {vmax}")
                plt.pause(0.01)
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
