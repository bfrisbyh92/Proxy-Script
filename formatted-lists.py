import subprocess
import os
import pyfiglet
import colorama
from colorama import Fore, Style, Back

# Initialize colorama
colorama.init()

## Made by Brendan Frisby
# Generate the ASCII art text using pyfiglet
myName = pyfiglet.figlet_format(
    "Bfrisbyh92")
# Print the ASCII art textx
print(Fore.BLACK + Back.BLUE , myName)

moveOver = ''' _____________
< moooooooove over >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
print(Fore.BLUE + Back.BLACK , moveOver + "\n This script will curl a fresh proxies, and then format them for the proxychains.conf file. After running it you will have two files configured for proxychains with hundreds and hundreds of free proxies automatically added to the config file. ")

# Set the URL for the socks4 list, HTTP, and a fresh proxychains.conf file.
socks4_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
http_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"

# Download the socks4 list using curl
subprocess.run(["curl", socks4_url, "-o", "socks4.txt"])
subprocess.run(["curl", http_url, "-o", "http.txt"])

# Reformat the socks4 list and save it to a new file
with open("socks4.txt") as f:
    lines = f.readlines()

formatted_lines = []
for line in lines:
    parts = line.strip().split(":")
    ip_address = parts[0]
    port = parts[1]
    formatted_line = f"socks4 {ip_address} {port}"
    formatted_lines.append(formatted_line)

with open("socks4_formatted.txt", "w") as f:
    for line in formatted_lines:
        f.write(line + "\n")

# Reformat the socks4 list and save it to a new file
with open("http.txt") as f:
    lines = f.readlines()

formatted_lines = []
for line in lines:
    parts = line.strip().split(":")
    ip_address = parts[0]
    port = parts[1]
    formatted_line = f"http {ip_address} {port}"
    formatted_lines.append(formatted_line)

with open("http_formatted.txt", "w") as f:
    for line in formatted_lines:
        f.write(line + "\n")

text = pyfiglet.figlet_format("Done...2 config files. \n in output \n  Use with \n  proxychains with  \n   -f flag.", 
font="small")
print(text)
