import yaml
from tpo.domain.data_domain import DataDomain
from tpo.config.config_manager import ConfigManager

def main():
    # Varible to Path to data_domain_finance.yaml in config folder
    config_path = "config/data_domain_finance.yaml"
    config_manager = ConfigManager()
    config_data = config_manager.load_config(config_path)

    domain_data = config_data["domain"]

    data_domain = DataDomain(
        name=domain_data["name"],
        abbreviation=domain_data["abbreviation"],
        zone=domain_data["zone"],
        description=domain_data["description"],
        location=domain_data["location"],
        owner=domain_data["owner"],
        tags=domain_data["tags"],
    )

    print("Created Data Domain:")
    print(data_domain)

if __name__ == "__main__":
    main()


# First Attempt: Working
# def main():
#     data_domain = DataDomain(
#         name="Financial Data Domain",
#         abbreviation="FDD",
#         zone="Data Processing",
#         description="A domain for financial data",
#         location="Global",
#         owner={"name": "John Doe", "email": "john.doe@example.com"},
#         tags=["finance", "banking", "data"],
#     )

#     print("Created Data Domain:")
#     print(data_domain)

if __name__ == "__main__":
    main()
