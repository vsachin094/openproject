from JinjaYamlRenderer import JinjaYAMLHandler
from Textfsm_Parser import TextFSMParser
JYRenderer = JinjaYAMLHandler()
# Call the function to convert YAML to a dictionary
yaml_file_path = "/home/sachin/projects/jinja_yaml_render/my_data.yaml"
yaml_data_str = JYRenderer.read_yaml_file(yaml_file_path)
result_dict = JYRenderer.yaml_to_dict(yaml_data_str)
print(result_dict)

template_file_path = "projects/jinja_yaml_render/template.jinja2"

template_string = JYRenderer.read_jinja_template(template_file_path)

print(template_string)

print(JYRenderer.render_template(template_string,result_dict))

parser = TextFSMParser()

template_path = "/home/sachin/projects/jinja_yaml_render/sample.textfsm"
raw_output = """
    eth0      Link encap:Ethernet  HWaddr 00:11:22:33:44:55  
            inet addr:192.168.1.100  Bcast:192.168.1.255  Mask:255.255.255.0

    eth1      Link encap:Ethernet  HWaddr 66:77:88:99:AA:BB  
            inet addr:10.0.0.1  Bcast:10.0.0.255  Mask:255.255.255.0

    lo        Link encap:Local Loopback  
            inet addr:127.0.0.1  Mask:255.0.0.0
"""

print(parser.convert_raw_to_structured(template_path,raw_output))