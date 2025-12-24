import tkinter as tk
from tkinter import messagebox
import random
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PingSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Utility Simulation")
        self.root.geometry("700x600")

        # GUI Elements
        self.ip_label = tk.Label(root, text="Enter IP Address:")
        self.ip_label.pack(pady=5)

        self.ip_entry = tk.Entry(root)
        self.ip_entry.insert(0, "192.168.1.1")
        self.ip_entry.pack(pady=5)

        self.ping_button = tk.Button(root, text="Start Ping", command=self.start_ping)
        self.ping_button.pack(pady=10)

        self.output_text = tk.Text(root, height=15, width=80)
        self.output_text.pack(pady=10)

        # Graph Setup
        self.fig = Figure(figsize=(6, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Ping Delay (ms)")
        self.ax.set_xlabel("Ping #")
        self.ax.set_ylabel("Delay")

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def start_ping(self):
        ip = self.ip_entry.get()
        total_pings = 12
        
        delays = []
        sent = 0
        received = 0

        self.output_text.delete(1.0, tk.END)
        self.ax.clear()
        self.ax.set_title("Ping Delay (ms)")
        self.ax.set_xlabel("Ping #")
        self.ax.set_ylabel("Delay")

        self.output_text.insert(tk.END, f"Pinging {ip} with 32 bytes of data...\n\n")

        for i in range(1, total_pings + 1):
            sent += 1
            self.output_text.insert(tk.END, f"Request {i} -> ")

            if random.random() < 0.2:
                self.output_text.insert(tk.END, "Request timed out.\n")
                delays.append(0)
            else:
                delay = round(random.uniform(1, 100), 2)
                self.output_text.insert(tk.END, f"Reply from {ip}: time={delay}ms\n")
                delays.append(delay)
                received += 1

            self.ax.plot(range(1, i + 1), delays, marker='o', color='blue')
            self.canvas.draw()
            self.root.update()
            time.sleep(1)

        lost = sent - received
        loss_percent = int((lost / sent) * 100)

        self.output_text.insert(tk.END, "\nPing statistics:\n")
        self.output_text.insert(tk.END, f"    Packets: Sent = {sent}, Received = {received}, Lost = {lost} ({loss_percent}% loss)\n")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PingSimulatorApp(root)
    root.mainloop()
