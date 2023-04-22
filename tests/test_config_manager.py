# TTD Test for a config manager

import pytest
from pathlib import Path
from config_manager import ConfigManager

CONFIG_FILE = Path(__file__).parent / "config.yanl"

def test_load_non_existing_file():
    conf_manager = ConfigManager(CONFIG_FILE)
    with pytest.raises(FileNotFoundError):
        conf_manager.load()
