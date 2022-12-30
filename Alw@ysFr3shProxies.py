import subprocess
import os

# Set the URLs for the socks4, socks5, and http lists
socks4_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
socks5_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
http_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
proxychains_url = "https://raw.githubusercontent.com/haad/proxychains/master/src/proxychains.conf"

# Create the output directory if it doesn't already exist
output_dir = "Alw@ysFr3shProxies"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the socks4 list
subprocess.run(["curl", socks4_url, "-o", os.path.join(output_dir, "socks4.txt")])

# Download the socks5 list
subprocess.run(["curl", socks5_url, "-o", os.path.join(output_dir, "socks5.txt")])

# Download the http list
subprocess.run(["curl", http_url, "-o", os.path.join(output_dir, "http.txt")])

subprocess.run(["wget", proxychains_url, "-o", os.path.join(output_dir, "proxychains.conf")])


# Iterate over the files in the output directory
for file in ["socks4.txt", "socks5.txt", "http.txt"]:
    # Determine the output file name based on the input file name
    output_file = "proxy" + file.capitalize().replace(".txt", ".conf")

    # Open the input and output files
    with open(os.path.join(output_dir, file), "r") as input_f, open(os.path.join(output_dir, output_file), "w") as output_f:
        # Iterate over the lines in the input file
        for line in input_f:
            # Split the line into the IP address and port
            ip, port = line.strip().split(":")

            # Write the reformatted line to the output file
            output_f.write(f"{file.replace('.txt', '')} {ip} {port}\n")

# Open the file we want to prepend to in write mode
with open("socks4.txt", "w") as output_f:
    # Open the file we want to prepend in read mode
    with open("proxychains.conf", "r") as input_f:
        # Iterate over the lines in the input file
        for line in input_f:
            # Prepend the line to the output file
            output_f.write(line)

    # Open the original file in read mode
    with open("socks4.txt", "r") as original_f:
        # Iterate over the lines in the original file
        for line in original_f:
            # Write the line to the output file
            output_f.write(line)

print("Done!")



