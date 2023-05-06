import pytest
from tpo.domain.base_class import BaseConfig, Kind

@pytest.fixture
def base_config():
    return BaseConfig(
        name="Test Config",
        kind=Kind.DOMAIN,
        tags=["test", "config"],
        version="1.0",
        location="US",
        owner="John Doe",
        description="Test Configuration"
    )


def test_base_config_properties(base_config):
    """Test creation"""
    assert base_config.name == "Test Config"
    assert base_config.kind == Kind.DOMAIN
    assert base_config.tags == ["test", "config"]
    assert base_config.version == "1.0"
    assert base_config.location == "US"
    assert base_config.owner == "John Doe"
    assert base_config.description == "Test Configuration"
    print("Success: Base Config created")

def test_base_config_string(base_config):
    assert str(base_config) == "Test Config (DOMAIN)"
