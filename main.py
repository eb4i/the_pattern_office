from pathlib import Path
from tpo.domain.data_domain import DataDomain
from tpo.config.config_manager import ConfigManager

def main():

    # Variable to hold the Path to the config file
    config_file = Path("tpo/config/data_domain_finance.yaml")
    config_manager = ConfigManager(Path(config_file))
    # config_manager.set_config_file(Path("data_domain.yaml"))
    config_data = config_manager.get("domain")

    data_domain = DataDomain(
        name=config_data["name"],
        abbreviation=config_data["abbreviation"],
        zone=config_data["zone"],
        description=config_data["description"],
        location=config_data["location"],
        owner=config_data["owner"],
        tags=config_data["tags"],
    )

    print(f"Created Data Domain: {data_domain.name}")
    print(data_domain)

if __name__ == "__main__":
    main()
