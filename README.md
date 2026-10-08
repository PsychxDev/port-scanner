# Port Scanner

A lightweight TCP port scanner written in Python using only the standard library.

The tool allows you to scan a custom range of ports on an IPv4 address and reports which ports are accepting TCP connections.

## Features

* IPv4 address validation
* Custom port range
* TCP port scanning
* Connection timeout handling
* Scan duration measurement
* Open port detection
* Basic service identification
* Input validation
* No external dependencies

## Requirements

* Python 3.x

The project uses only Python's standard library:

```text
socket
time
ipaddress
```

## Usage

Run the program with:

```bash
python3 port_scanner.py
```

You will be prompted to enter the target IPv4 address and the port range.

Example:

```text
==========================
       Port Scanner
==========================
IP: 127.0.0.1
==========================
Scan starts from: 1
Scan ends at: 1000
==========================
Scanning ports between 1 and 1000....
```

Example result:

```text
=================
Scan took 0.8s
=================
2 Ports Found
Port: 22 (ssh)
Port: 80 (http)
```

If no open ports are detected:

```text
No Ports Found
```

## How It Works

For every port in the selected range, the scanner creates a TCP socket and attempts to establish a connection.

A return value of `0` from `connect_ex()` indicates that the connection was successful:

```python
res = sock.connect_ex((ip, port))

if res == 0:
    ports.append(port)
```

Each connection has a timeout of 0.5 seconds.

After scanning, the program uses `socket.getservbyport()` to retrieve the service commonly associated with each detected port.

## Limitations

* Scans TCP ports only.
* Ports are scanned sequentially.
* No UDP scanning.
* No multithreading or asynchronous scanning.
* No advanced service or version detection.
* Large port ranges may take longer to complete.

## Project Structure

```text
port-scanner/
└── port_scanner.py
```

## Purpose

This project was created to practice Python socket programming and understand the basics of TCP connections and port scanning.

It also provides practical experience with:

* Functions
* Loops
* Exception handling
* Input validation
* Sockets
* IPv4 addresses
* TCP connections
* Execution time measurement
* Command-line interfaces

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan systems and IP addresses that you own or have explicit permission to test.

The author is not responsible for misuse of this software.

## License

MIT License

