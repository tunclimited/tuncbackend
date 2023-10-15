import json
import os

# Load your Swagger JSON file
swagger_file = 'src/common/swagger.json'
with open(swagger_file, 'r') as f:
    swagger_data = json.load(f)

# Create a models folder if it doesn't exist
models_folder = 'build/models'
os.makedirs(models_folder, exist_ok=True)

# Access the "components" section to extract schemas
components = swagger_data.get('components', {})
schemas = components.get('schemas', {})

# Loop through the schemas in the "components" section and generate Python classes
for schema_name, schema_data in schemas.items():
    # Create a list to store property names and their data types
    properties_list = []

    # Extract properties from the schema
    properties = schema_data.get('properties', {})
    for prop_name, prop_data in properties.items():
        prop_type = prop_data.get('type', 'str')  # Default to 'str' if type is not specified
        properties_list.append((prop_name, prop_type))

    # Generate the Python class with a single __init__ method
    class_code = f'class {schema_name}:\n'
    class_code += f'    def __init__(self, '
    class_code += ', '.join([f'{prop_name}' for prop_name, prop_type in properties_list])
    class_code += '):\n'
    for prop_name, prop_type in properties_list:
        class_code += f'        # {prop_type}: {prop_name}\n'
        class_code += f'        self.{prop_name} = {prop_name}\n\n'

    # Add the to_dict method to convert the object to a dictionary
    class_code += f'    def to_dict(self):\n'
    class_code += f'        return {{\n'
    for prop_name, _ in properties_list:
        class_code += f'            "{prop_name}": self.{prop_name},\n'
    class_code += f'        }}\n'

    # Save the Python class to a Python file in the models folder
    model_file = os.path.join(models_folder, f'{schema_name}.py')
    with open(model_file, 'w') as f:
        f.write(class_code)

print("Models generated and saved in the 'models' folder.")
