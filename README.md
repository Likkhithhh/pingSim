# Ping Utility Simulator

A Python networking-learning project that simulates ping behavior from both the command line and a desktop GUI.

> This is a **simulation**. It does not send real ICMP packets over the network.

## Features

- Configurable destination IP address
- Simulated packet transmission and packet loss
- Randomized round-trip delay values
- Sent/received/lost packet statistics
- Tkinter desktop interface
- Matplotlib latency graph

## Files

- `ping_sim.py` — command-line ping simulation
- `ping_gui.py` — Tkinter GUI with a live latency graph

## Requirements

- Python 3
- Matplotlib for the GUI version

Install the GUI dependency:

```bash
python3 -m pip install matplotlib
```

## Run

Command-line simulation:

```bash
python3 ping_sim.py
```

GUI simulation:

```bash
python3 ping_gui.py
```

## Learning focus

This project demonstrates packet-loss concepts, latency visualization, basic networking statistics, Python GUI development, and event-driven application design.
