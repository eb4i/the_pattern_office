# import pytest
# from pathlib import Path
# from tpo.application.config_manager import ConfigManager

# @pytest.fixture
# def conf_manager(tmp_path):
#     config_file = tmp_path / "config.yaml"
#     config_manager = ConfigManager(config_file)
#     return config_manager

# class TestConfigManager:
#     def test_create_config_manager(self, conf_manager):
#         """Test creating a ConfigManager"""
#         assert conf_manager.config_file.exists() == False
#         print("Success: ConfigManager created")

#     def test_load_non_existing_file(self, conf_manager):
#         """Test loading a non-existing file"""
#         with pytest.raises(FileNotFoundError):
#             conf_manager.load()
#         print("Success: FileNotFoundError raised for non-existing file")

#     def test_load_not_a_file(self, tmp_path, conf_manager):
#         """Test loading when not a file"""
#         not_a_file = tmp_path / "not_a_file"
#         not_a_file.mkdir()

#         conf_manager.config_file = not_a_file
#         with pytest.raises(ValueError):
#             conf_manager.load()
#         print("Success: ValueError raised for a non-file path")

#     def test_load_invalid_yaml(self, conf_manager):
#         """Test loading an invalid YAML file"""
#         conf_manager.config_file.write_text("{invalid", encoding="utf-8")
#         with pytest.raises(ValueError):
#             conf_manager.load()
#         print("Success: ValueError raised for invalid YAML")

#     def test_load_valid_yaml(self, conf_manager):
#         """Test loading a valid YAML file"""
#         conf_manager.config_file.write_text("{'valid': 'yaml'}", encoding="utf-8")
#         conf_manager.load()
#         assert conf_manager.config == {"valid": "yaml"}
#         print("Success: Valid YAML loaded")

#     def test_get(self, conf_manager):
#         """Test getting a value from the config"""
#         conf_manager.config_file.write_text("{'valid': 'yaml'}", encoding="utf-8")
#         conf_manager.load()
#         assert conf_manager.get("valid") == "yaml"
#         assert conf_manager.get("invalid") is None
#         assert conf_manager.get("invalid", "default") == "default"
#         print("Success: Get method works as expected")

#     def test_set(self, conf_manager):
#         """Test setting a value in the config"""
#         conf_manager.config_file.write_text("{'valid': 'yaml'}", encoding="utf-8")
#         conf_manager.load()
#         conf_manager.set("new", "value")
#         assert conf_manager.get("new") == "value"
#         print("Success: Set method works as expected")
