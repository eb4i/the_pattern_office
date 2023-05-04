import logging
from pathlib import Path
from tpo.application.config_manager import ConfigManager
from tpo.domain.data_domain import DataDomain

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the paths to the configuration files for each type
data_domain_file = Path("tpo/config/data_domain_finance.yaml")

# Create ConfigManager instances for each configuration file
logger.info("Creating ConfigManager instances for each configuration file")
data_domain_config = ConfigManager(data_domain_file)

# Load the configurations
logger.info("Loading configurations")
data_domain_config.load()

# Print the loaded YAML
logger.info("Loaded YAML:\n%s", data_domain_config.config)

# Extract the Data Domain configuration
logger.info("Extracting the Data Domain configuration")
data_domain_config = data_domain_config.get("domain")
name = data_domain_config.get("name")
abbreviation = data_domain_config.get("abbreviation")
zone = data_domain_config.get("zone")
description = data_domain_config.get("description")
distribution = data_domain_config.get("distribution")
version = data_domain_config.get("version")
location = data_domain_config.get("location")
owner = data_domain_config.get("owner")
tags = data_domain_config.get("tags")
logger.info("Data Domain configuration extracted")

# Create a Data Domain instance
logger.info("Creating a Data Domain instance")
data_domain = DataDomain(
    name=name,
    location=location,
    owner=owner,
    tags=tags,
    description=description,
    zone=zone,
    abbreviation=abbreviation
)

# Display the Data Domain instance
logger.info("Displaying the Data Domain instance")
data_domain.display()

# Perform CRUD operations on the configurations
# For example, read a value from the Data Domain configuration
logger.info("Reading a value from the Data Domain configuration")
domain_name = data_domain_config.get("domain.name")
logger.info("Domain Name: %s", domain_name)

# Save the updated configurations to their respective YAML files
logger.info("Saving updated configurations to their respective YAML files")
# data_domain_config.save()
logger.info("Configurations saved")


# Prior work
# Define the paths to the configuration files for each type
# data_domain_file = Path("tpo/config/data_domain_finance.yaml")
# Logger Info for data_domain_file

# logger.info("data_domain_file: %s", data_domain_file)
# data_product_file = Path("path/to/data_product.yaml")
# pattern_file = Path("path/to/pattern.yaml")

# Create ConfigManager instances for each configuration file
# data_domain_config = ConfigManager(data_domain_file)
# Logger Info for data_domain_config created
# logger.info("created ConfigManager")

# data_product_config = ConfigManager(data_product_file)
# pattern_config = ConfigManager(pattern_file)

# Load the configurations
# data_domain_config.load()
# data_product_config.load()
# pattern_config.load()

# Perform CRUD operations on the configurations
# For example, read a value from the Data Domain configuration
# domain_name = data_domain_config.get("domain.name")
# print(data_domain_config.config)
# Update a value in the Data Product configuration
# data_product_config.set("product.name", "new_product_name")

# Save the updated configurations to their respective YAML files
# data_domain_config.save()
# data_product_config.save()
# pattern_config.save()
