import hcl2

def extract_variables(tf_file_path):
    with open(tf_file_path, 'r') as tf_file:
        content = tf_file.read()

        # Parse the HCL content
        parsed_content = hcl2.loads(content)

        # Extract variable names
        variables = parsed_content.get("variable", {}).keys()

        return variables

# Example usage:
terraform_file_path = 'path/to/your/terraform/file.tf'
variable_names = extract_variables(terraform_file_path)

print("Variable Names:")
for variable in variable_names:
    print(variable)
