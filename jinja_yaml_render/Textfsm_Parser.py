import textfsm

class TextFSMParser:

    def convert_raw_to_structured(self, template_path, raw_output):
        """
        Convert raw text output using the TextFSM template to structured data.

        Args:
            template_path (str): The path to the TextFSM template file.
            raw_output (str): The raw text output to be parsed.

        Returns:
            list: A list of dictionaries containing structured data.
            None: If an error occurs during parsing.
        """
        try:
            # Load the TextFSM template
            with open(template_path) as template_file:
                fsm_template = textfsm.TextFSM(template_file)

            # Parse the raw output using the template
            structured_data = fsm_template.ParseText(raw_output)

            # Convert the parsed data to a list of dictionaries
            structured_data_list = [dict(zip(fsm_template.header, entry)) for entry in structured_data]

            return structured_data_list

        except FileNotFoundError:
            print(f"Template file '{template_path}' not found.")
            return None
        except textfsm.TextFSMError as e:
            print(f"An error occurred: {str(e)}")
            return None

    def textfsm_template_validation(template_path):
        """
        Check if a TextFSM template is valid.

        Args:
            template_path (str): The path to the TextFSM template file.

        Returns:
            bool: True if the template is valid, False otherwise.
        """
        try:
            # Attempt to load the TextFSM template
            with open(template_path) as template_file:
                textfsm.TextFSM(template_file)
            return True
        except FileNotFoundError:
            print(f"Template file '{template_path}' not found.")
            return False
        except textfsm.TextFSMError as e:
            print(f"Template validation error: {str(e)}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False



   