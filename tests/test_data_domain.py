# Create a set of test cases for the DataDomain class

# Path: tests\test_data_domain.py
import pytest
from tpo.domain.data_domain import DomainConfig

# Create a fixture for the DomainConfig class
@pytest.fixture
def domain_config():
    return DomainConfig(
        name="Test Config",
        kind="DOMAIN",
        tags=["test", "config"],
        version="1.0",
        location="US",
        owner="John Doe",
        description="Test Configuration",
        url="https://www.test.com",
        abbreviation="TEST",
        zone="test",
    )

# Create a test case for the DomainConfig class
def test_domain_config_properties(domain_config):
    """Test creation"""
    assert domain_config.name == "Test Config"
    assert domain_config.kind == "DOMAIN"
    assert domain_config.tags == ["test", "config"]
    assert domain_config.version == "1.0"
    assert domain_config.location == "US"
    assert domain_config.owner == "John Doe"
    assert domain_config.description == "Test Configuration"
    assert domain_config.url == "https://www.test.com"
    assert domain_config.abbreviation == "TEST"
    assert domain_config.zone == "test"
    print("Success: Domain Config created")

# Create a test case for the print function
def test_domain_config_string(domain_config):
    assert str(domain_config) == "Test Config (DOMAIN) with url https://www.test.com, abbreviation TEST, and zone test"
    print("Success: Domain Config string created")