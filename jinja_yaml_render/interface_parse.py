import re

# Sample 'show interfaces' output
show_interfaces_output = """
Interface GigabitEthernet1/0/1
    Description: Connection to Server
    Status: Up
    Speed: 1000 Mbps

Interface GigabitEthernet1/0/2
    Description: Connection to Switch
    Status: Up
    Speed: 1000 Mbps

Interface GigabitEthernet1/0/3
    Description: Connection to Printer
    Status: Down
    Speed: 1000 Mbps
"""

# Define a regex pattern to match the start of each interface section
interface_pattern = r'Interface (\S+)'

# Use the findall method to find all interface sections
interface_sections = re.findall(interface_pattern, show_interfaces_output)

# Initialize a list to store the lines for each interface
interface_lines_list = []

# Iterate through the interface sections and store the lines in the list
for interface_name in interface_sections:
    # Create a regex pattern to match the section from start to end
    section_pattern = rf'Interface {re.escape(interface_name)}(.*?)\n\n|Interface {re.escape(interface_name)}(.*)$'
    
    # Use re.search to find the section in the output
    match = re.search(section_pattern, show_interfaces_output, re.DOTALL)
    
    if match:
        # Extract and store the matched section (including the start pattern)
        section = match.group(0)
        
        # Split the section into lines and store them in the list
        lines = section.strip().split('\n')
        interface_lines_list.append(lines)

# Now you have a list of lists where each inner list contains the lines for an interface
# For example, to access the lines for GigabitEthernet1/0/1:
# gigabit_eth1_0_1_lines = interface_lines_list[0]
print(interface_lines_list)
# You can do the same for other interfaces as well
