import subprocess

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

# Concatenate the contents of socks4_formatted.txt to the end of proxychains.conf
#subprocess.run(['cat', 'socks4_formatted.txt', '>>', 'proxySocks4.conf'], stdout=subprocess.PIPE, 
#stderr=subprocess.PIPE, universal_newlines=True)

# Concatenate the contents of http_formatted.txt to the end of proxychains.conf
#subprocess.run(['cat', 'http_formatted.txt', '>>', 'proxyHttp.conf'], stdout=subprocess.PIPE,
#stderr=subprocess.PIPE, universal_newlines=True)

#subprocess.run(['rm', '-rf', 'socks4.txt', 'http.txt', 'socks4_formatted.txt', 'http_formatted.txt'], 
#stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#universal_newlines=True)
