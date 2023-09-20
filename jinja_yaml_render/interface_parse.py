import re

# Sample 'show interfaces bundle-ether *' output
show_interfaces_bundle_ether_output = """
Bundle-Ether1 line protocol is admin down
    Description: Connection to Server
    Status: Up
    Speed: 10000 Mbps

Bundle-Ether2 line protocol is admin up
    Description: Connection to Switch
    Status: Up
    Speed: 10000 Mbps

Bundle-Ether3 line protocol is up
    Description: Connection to Printer
    Status: Down
    Speed: 1000 Mbps
"""

# Define a regex pattern to match the "Bundle-Ether" interfaces and their lines
bundle_ether_pattern = r'Bundle-Ether\S+.*?(?=\nBundle-Ether|\Z)'

# Use re.findall to extract each "Bundle-Ether" section
bundle_ether_sections = re.findall(bundle_ether_pattern, show_interfaces_bundle_ether_output, re.DOTALL)

# Initialize a list to store the raw lines for each "Bundle-Ether" interface
bundle_ether_lines_list = []

# Iterate through the "Bundle-Ether" sections and store the raw lines in the list
for section in bundle_ether_sections:
    lines = section.strip().split('\n')
    bundle_ether_lines_list.append(lines)

# Now you have a list of lists where each inner list contains the raw lines for a "Bundle-Ether" interface
# For example, to access the raw lines for Bundle-Ether1:
bundle_eth1_lines = bundle_ether_lines_list[0]
print(bundle_eth1_lines)
# You can do the same for other "Bundle-Ether" interfaces as well
