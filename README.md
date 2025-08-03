# Minecraft Bedrock Server Stress Tester GUI

**Minecraft Bedrock Server Stress Tester GUI** is a robust, easy-to-use tool designed for server administrators, developers, and hosting providers to evaluate the resilience and network performance of Minecraft Bedrock Edition servers.  
It simulates high-volume UDP traffic from an external client machine, allowing realistic stress testing and monitoring of server capacity under load.

---

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)   
- [How It Works](#how-it-works)  
- [Warnings and Legal](#warnings-and-legal)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **Graphical User Interface (GUI):** Built using Python's `tkinter` for intuitive control and real-time feedback.  
- **High-Volume UDP Flooding:** Simultaneously sends thousands of UDP packets to the target Bedrock server port to simulate intense network load.  
- **Live Statistics:** Displays packets sent, bandwidth usage estimation, test duration, and thread count in real-time.  
- **Customizable Settings:** Easily configure target IP, port, number of threads, packet size, and test duration to tailor the test to your needs.  
- **Lightweight and Portable:** Requires only Python 3.8+ without heavy dependencies.  
- **Open Source:** Fully transparent and extensible to suit advanced testing scenarios.

---

## Requirements

- Python 3.8 or newer  
- No additional external Python libraries required (uses built-in modules: `tkinter`, `socket`, `threading`, `time`, `random`)

---

## Installation

Clone the repository or download the latest release:

```bash
git clone https://github.com/Parsmehr345/minecraft-bedrock-stress-tester.git
cd minecraft-bedrock-stress-tester
```

## Usage

Run the stress tester script with Python:

python stress_tester.py

The GUI will prompt you for:

    Server IP: The public IP address or hostname of your Minecraft Bedrock server.

    Port: Typically 19132 unless customized.

    Threads: Number of concurrent worker threads sending UDP packets (higher means more load).

    Packet Size: Size in bytes of each UDP packet sent (default recommended is 25 bytes).

    Test Duration: How long (in seconds) the stress test will run.

Click Start to begin the test. Real-time statistics will update on screen. Click Stop to end the test manually.
Configuration

Adjust settings according to your testing environment:
Parameter	Description	Default
Server IP	Target server IP or hostname	None
Port	Target UDP port (Minecraft Bedrock default: 19132)	19132
Threads	Number of parallel sender threads	50
Packet Size	Size in bytes of each UDP packet	25
Duration	Length of test in seconds (0 for unlimited)	0

## How It Works

This tool creates multiple threads, each opening a UDP socket that sends continuous streams of packets to the target server’s port. It does not simulate full client login or gameplay but floods the network layer to evaluate server packet handling and network stack resilience.

By measuring packets sent and timing, you can estimate your server’s capacity and network bottlenecks.
Limitations

    Does not simulate full Minecraft Bedrock protocol or client behavior (no login, no gameplay).

    UDP flooding might be blocked by firewall, anti-DDoS services, or hosting provider protections.

    Should only be used for testing servers you own or have explicit permission to test.

    Network latency and packet loss may affect test accuracy.

## Warnings and Legal

    ⚠️ Important: This tool must be used responsibly and legally.
    Unauthorized stress testing or flooding of servers you do not own or have permission to test is illegal and unethical and may result in legal consequences.
    Always obtain proper authorization before conducting any stress tests.

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit pull requests for:

    Adding protocol-level client simulation

    Detailed bandwidth measurement and logging

    Graphical bandwidth charts with matplotlib or similar

    Multi-platform packaging (e.g., executable builds)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
License

