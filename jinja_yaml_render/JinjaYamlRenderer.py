from jinja2 import Template, Environment, exceptions, TemplateError
import yaml

class JinjaYAMLHandler:

    def __init__(self):
        self.env = Environment()
    def render_template(self, template_string, data):
        """
        Render a Jinja2 template with the provided data.

        Args:
            template_string (str): The Jinja2 template as a string.
            data (dict): The data to pass to the template.

        Returns:
            str: The rendered template output as a string, or None if an error occurs.
        """
        try:
            # Create a Jinja2 Template object from the template string
            if (self.validate_template(template_string)):
                template = self.env.from_string(template_string)
                rendered_output = template.render(data)
                return rendered_output
        except TemplateError as e:
            print(f"Jinja2 template rendering error: {str(e)}")
            return None


    def read_jinja_template(self,file_path):
        """
        Read a Jinja2 template from a file and return it as a template string.

        Args:
            file_path (str): The path to the Jinja2 template file.

        Returns:
            str: The Jinja2 template as a template string.
            None: If the file cannot be found or an error occurs.
        """
        try:
            with open(file_path, "r") as template_file:
                template_string = template_file.read()

            if (self.validate_template(template_string)):
                return template_string
        
        except FileNotFoundError:
            print(f"Jinja2 template file '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def validate_template(self, template_string):
        """
        Validate a Jinja2 template string.

        Args:
            template_string (str): The Jinja2 template as a string.

        Returns:
            bool: True if the template is valid, False otherwise.
            str: If the template is invalid, returns the error message.
        """
        try:
            Environment().parse(template_string)
            return True
        except exceptions.TemplateSyntaxError as e:
            print(f"Jinja2 template validation error: {str(e)}")
            return False

    def validate_yaml(self, yaml_string):
        """
        Validate YAML data.

        Args:
            yaml_string (str): The YAML data as a string.

        Returns:
            bool: True if the YAML is valid, False otherwise.
            str: If the YAML is invalid, returns the error message.
        """
        try:
            yaml.safe_load(yaml_string)
            return True
        except yaml.YAMLError as e:
            print(f"YAML validation error: {str(e)}")
            return False
        
    def read_yaml_file(self,file_path):
        """
        Read a YAML file and return its content as a string.

        Args:
            file_path (str): The path to the YAML file.

        Returns:
            str: The YAML content as a string.
            None: If the file cannot be found or an error occurs.
        """
        try:
            with open(file_path, "r") as yaml_file:
                yaml_str = yaml_file.read()
            if (self.validate_yaml(yaml_str)):
                return yaml_str
        except FileNotFoundError:
            print(f"YAML file '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def yaml_to_dict(self,yaml_str):
        """
        Convert a YAML string to a Python dictionary.

        Args:
            yaml_str (str): The YAML data as a string.

        Returns:
            dict: The YAML data as a Python dictionary.
            None: If an error occurs while parsing the YAML data.
        """
        try:
            data_dict = yaml.safe_load(yaml_str)
            return data_dict
        except yaml.YAMLError as e:
            print(f"An error occurred while parsing the YAML data: {str(e)}")
            return None
