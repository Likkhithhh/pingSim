# Ping Utility Simulator

[![Python syntax check](https://github.com/Likkhithhh/pingSim/actions/workflows/python-syntax.yml/badge.svg)](https://github.com/Likkhithhh/pingSim/actions/workflows/python-syntax.yml)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![Networking](https://img.shields.io/badge/Topic-Networking-success)

A Python networking-learning project that simulates ping behavior from both the command line and a desktop GUI.

> **Important:** this is a simulation. It does not send real ICMP packets.

## Why this project matters

The project turns networking concepts—latency, packet loss, sent/received counts, and basic availability statistics—into an interactive Python application.

## Features

- Configurable destination IP address
- Simulated packet transmission and packet loss
- Randomized round-trip delay values
- Sent/received/lost packet statistics
- Tkinter desktop interface
- Matplotlib latency graph
- CLI and GUI implementations

## Architecture

```text
Destination IP
     ↓
Ping simulation loop
     ↓
Random loss + latency model
     ↓
Packet statistics
     ↓
CLI output / GUI graph
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run

CLI:

```bash
python3 ping_sim.py
```

GUI:

```bash
python3 ping_gui.py
```

## Learning focus

- Packet loss and latency concepts
- Networking statistics
- Python GUI development
- Matplotlib visualization
- Event-driven application design

## Roadmap

- Add a real ICMP mode using the system `ping` command
- Add deterministic simulation parameters
- Add automated unit tests
- Export latency results to CSV


---

## Portfolio navigation

Explore the rest of my GitHub portfolio:

- [QOS-VIDEO](https://github.com/Likkhithhh/QOS-VIDEO) — machine-learning experiments for video-streaming QoS optimization
- [weatherAPP](https://github.com/Likkhithhh/weatherAPP) — browser weather dashboard using public APIs
- [pingSim](https://github.com/Likkhithhh/pingSim) — Python networking and latency simulator
- [lexgen](https://github.com/Likkhithhh/lexgen) — educational lexer-generator and compiler-design project
- [ATTENDENCEBOT](https://github.com/Likkhithhh/ATTENDENCEBOT) — face-recognition reference work for an attendance-system portfolio project
- **READS — North Karnataka Student Dropout Risk System** — Python/AI/ML internship project at Rural Education and Action Development Society (READS), 03 Aug–03 Sep 2026; focused on student-attribute analysis, preprocessing, dropout-risk prediction, model evaluation, and results

**GitHub:** [Likkhithhh](https://github.com/Likkhithhh)
