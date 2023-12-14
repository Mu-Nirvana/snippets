import re

def extract_variables(tf_file_path):
    with open(tf_file_path, 'r') as tf_file:
        content = tf_file.read()

    # Use regular expression to find variable declarations
    variable_pattern = re.compile(r'\bvariable\s+"([^"]+)"\s*{')
    variables = variable_pattern.findall(content)

    return variables

# Example usage:
terraform_file_path = 'test.tf'
variable_names = extract_variables(terraform_file_path)


for variable_assignment in variable_names:
    print(variable_assignment + " = var." + variable_assignment)