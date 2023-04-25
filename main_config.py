from pathlib import Path
from tpo.application.config_manager import ConfigManager

# Define the paths to the configuration files for each type
data_domain_file = Path("path/to/data_domain.yaml")
# data_product_file = Path("path/to/data_product.yaml")
# pattern_file = Path("path/to/pattern.yaml")

# Create ConfigManager instances for each configuration file
data_domain_config = ConfigManager(data_domain_file)
# data_product_config = ConfigManager(data_product_file)
# pattern_config = ConfigManager(pattern_file)

# Load the configurations
data_domain_config.load()
# data_product_config.load()
# pattern_config.load()

# Perform CRUD operations on the configurations
# For example, read a value from the Data Domain configuration
domain_name = data_domain_config.get("domain.name")

# Update a value in the Data Product configuration
# data_product_config.set("product.name", "new_product_name")

# Save the updated configurations to their respective YAML files
data_domain_config.save()
# data_product_config.save()
# pattern_config.save()
