# TTD Test for a config manager

import pytest
from pathlib import Path
from config_manager import ConfigManager

CONFIG_FILE = Path(__file__).parent / "config.yanl"

def test_load_non_existing_file():
    conf_manager = ConfigManager(CONFIG_FILE)
    with pytest.raises(FileNotFoundError):
        conf_manager.load()

# Test load not a file
def test_load_not_a_file(tmpdir):
    not_a_file = tmpdir / "not_a_file"
    # not_a_file = Path(__file__).parent / "not_a_file"
    not_a_file.mkdir()

    conf_manager = ConfigManager(not_a_file)
    with pytest.raises(ValueError):
        conf_manager.load()

# Test load invalid yaml
def test_load_invalid_yaml(tmpdir):
    invalid_yaml = tmpdir / "invalid.yaml"
    # invalid_yaml = Path(__file__).parent / "invalid_yaml"
    invalid_yaml.write_text("{invalid", encoding="utf-8")

    conf_manager = ConfigManager(invalid_yaml)
    with pytest.raises(ValueError):
        conf_manager.load()
