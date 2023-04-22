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

# Test load valid yaml
def test_load_valid_yaml(tmpdir):
    valid_yaml = tmpdir / "valid.yaml"
    valid_yaml.write_text("{'valid': 'yaml'}", encoding="utf-8")

    conf_manager = ConfigManager(valid_yaml)
    conf_manager.load()
    assert conf_manager.config == {"valid": "yaml"}

# Test get
def test_get(tmpdir):
    valid_yaml = tmpdir / "valid.yaml"
    valid_yaml.write_text("{'valid': 'yaml'}", encoding="utf-8")

    conf_manager = ConfigManager(valid_yaml)
    conf_manager.load()
    assert conf_manager.get("valid") == "yaml"
    assert conf_manager.get("invalid") is None
    assert conf_manager.get("invalid", "default") == "default"

# Test set
def test_set(tmpdir):
    valid_yaml = tmpdir / "valid.yaml"
    valid_yaml.write_text("{'valid': 'yaml'}", encoding="utf-8")

    conf_manager = ConfigManager(valid_yaml)
    conf_manager.load()
    conf_manager.set("new", "value")
    assert conf_manager.get("new") == "value"
#TODO: Test save
# def test_set_and_save(tmpdir):
#     test_yaml = tmpdir / "test.yaml"

#     config_manager = ConfigManager(test_yaml)
#     config_manager.set("key", "value")
#     # config_manager.save()

#     assert test_yaml.read_text() == "key: value\n"

# Test set and save
# def test_set(tmpdir):
#     valid_yaml = tmpdir / "valid.yaml"
#     valid_yaml.write_text("{'valid': 'yaml'}", encoding="utf-8")

#     conf_manager = ConfigManager(valid_yaml)
#     conf_manager.load()
#     conf_manager.set("new", "value")
#     conf_manager.save()
#     assert valid_yaml.read_text(encoding="utf-8") == "{'new': 'value\n'}"

# def test_save(tmpdir):
#     valid_yaml = tmpdir / "valid.yaml"
#     valid_yaml.write_text("{'valid': 'yaml'}", encoding="utf-8")

#     conf_manager = ConfigManager(valid_yaml)
#     conf_manager.load()
#     conf_manager.set("new", "value")
#     conf_manager.save(valid_yaml)
#     assert valid_yaml.read_text(encoding="utf-8") == "{'new': 'value'}"

