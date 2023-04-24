from pathlib import Path
from tpo.domain.data_domain import DataDomain
from tpo.config.config_manager import ConfigManager
from tpo.patterns.data_tier import DataTierPattern
from tpo.application.pattern_factory import PatternFactory

def main():

    yaml_pattern = '''
    pattern:
        metadata:
            name: 'datatier'
            display_name: 'Data Tier'
            type: 'structural'
            version: '0.1'
            description: 'The data tier path pattern'
            usage: ['transformation', 'serving']
            example: 'How it looks when used go’s here'
        definition:
            tiers: ['raw', 'cleansed', 'curated']
        storage:
            objects: ['folder']
            template: '{container}/{tier}/{zone}/{domain}/{system}/{dataset}'
        serving:
            objects: ['schema']
    '''

    # Create a Data Domain and add patterns
    data_domain = DataDomain("Data Domain")
    data_domain.add_pattern(data_tier_pattern)

# Create a Data Product referencing the Data Domain
    data_product = DataProduct("Data Product", data_domain)


# Create a DataTierPattern instance from the YAML string
    data_tier_pattern = PatternFactory.create_pattern_from_yaml(yaml_pattern)
    print(data_tier_pattern)

# Register the DataTierPattern in the PatternFactory
    factory = PatternFactory()
    factory.register_pattern("DataTier", DataTierPattern)

# Create a DataDomain
    data_domain = DataDomain(
        name="domain_name",
        abbreviation="domain_abbrev",
        zone="zone_name",
        description="Test Description",
        location="Global",
        owner={"name": "owner_name", "email": "owner_email"},
        tags=["tag1", "tag2"],
        pattern_factory=factory,
    )

    # Add a DataTierPattern to the DataDomain
    data_domain.add_pattern("DataTier", tiers=["raw", "cleansed", "curated"])

    # Add a second DataTierPattern to the DataDomain
    data_domain.add_pattern("DataTier", tiers=["stage1", "stage2", "stage3"])


    # Variable to hold the Path to the config file: WORKING
    # config_file = Path("tpo/config/data_domain_finance.yaml")
    # config_manager = ConfigManager(Path(config_file))
    # config_data = config_manager.get("domain")

    # data_domain = DataDomain(
    #     name=config_data["name"],
    #     abbreviation=config_data["abbreviation"],
    #     zone=config_data["zone"],
    #     description=config_data["description"],
    #     location=config_data["location"],
    #     owner=config_data["owner"],
    #     tags=config_data["tags"],
    # )

    print(f"Created Data Domain: {data_domain.name}")
    print(data_domain)

if __name__ == "__main__":
    main()
