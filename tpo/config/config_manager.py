# A Config Manager for Configuration as Code in YAML

import yaml
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file: Path):
        self.config_file = config_file
        self.config = None

    def load(self):
        if self.config_file is None:
            raise ValueError("Config file not set")
        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file {self.config_file} not found")
        if not self.config_file.is_file():
            raise ValueError(f"Config file {self.config_file} is not a file")

        with open(self.config_file, "r") as f:
            try:
                self.config = yaml.load(f, Loader=yaml.FullLoader)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing config file {self.config_file}: {e}")

            # return yaml.load(f, Loader=yaml.FullLoader)

    # def save(self, config):
    #     with open(self.config_file, "w") as f:
    #         yaml.dump(config, f)

    # Get a value from the config
    def get(self, key: str, default=None):
        if self.config is None:
            self.load()
        return self.config.get(key, default)
    # Set a value in the config
    def set(self, key: str, value):
        if self.config is None:
            self.load()
        self.config[key] = value
        self.save(self.config)
    
    # Save the config or optionally pass in a config to save
    def save(self, config=None):
        if config is None:
            config = self.config
        with open(self.config_file, "w") as f:
            yaml.safe_dump(config, f)
    
    # def save(self, config):
    #     with open(self.config_file, "w") as f:
    #         yaml.dump(config, f)