import os
import yaml

# Define the path to the configuration directory and file
config_dir = "conf"
config_file = os.path.join(config_dir, "config.yaml")

# Ensure the configuration directory exists
os.makedirs(config_dir, exist_ok=True)

# Define the content of the YAML configuration file
config_content = {
    "defaults": [
        "_self_"
    ],
    "model": {
        "type": "some_model_type",
        "parameters": {
            "param1": 1,
            "param2": "default_value"
        }
    }
}

# Write the YAML content to the file
with open(config_file, "w") as file:
    yaml.dump(config_content, file, default_flow_style=False)

print(f"Configuration file created at {config_file}")