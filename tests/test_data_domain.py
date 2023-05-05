import pytest
from tpo.domain.data_domain import DataDomain
from tpo.application.pattern_factory import PatternFactory

@pytest.fixture
def data_domain():
    return DataDomain(
        name="domain_name",
        abbreviation="domain_abbrev",
        zone="zone_name",
        description="Test Description",
        distribution="Test Distribution",
        version="Test Version",
        location="Global",
        owner={"name": "owner_name", "email": "owner_email"},
        tags=["tag1", "tag2"],
    )

@pytest.fixture
def sample_pattern_class():
    class SamplePattern:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    return SamplePattern

class TestDataDomain:
    def test_data_domain_creation(self, data_domain):
        """Test DataDomain creation"""
        assert data_domain.name == "domain_name"
        assert data_domain.abbreviation == "domain_abbrev"
        assert data_domain.zone == "zone_name"
        assert data_domain.description == "Test Description"
        assert data_domain.location == "Global"
        assert data_domain.owner == {"name": "owner_name", "email": "owner_email"}
        assert data_domain.tags == ["tag1", "tag2"]
        print("Success: DataDomain created")

    def test_add_pattern(self, data_domain):
        """Test adding a pattern to the DataDomain"""
        data_domain.add_pattern("pattern1")
        assert data_domain.patterns == ["pattern1"]

        data_domain.add_pattern("pattern2")
        assert data_domain.patterns == ["pattern1", "pattern2"]
        print("Success: Pattern added to DataDomain")

    def test_add_data_product(self, data_domain):
        """Test adding a data product to the DataDomain"""
        data_domain.add_data_product("data_product1")
        assert data_domain.data_products == ["data_product1"]

        data_domain.add_data_product("data_product2")
        assert data_domain.data_products == ["data_product1", "data_product2"]
        print("Success: Data product added to DataDomain")

    # def test_add_pattern(data_domain, sample_pattern_class):
    #     data_domain.add_pattern(sample_pattern_class("value1", "value2"))
    #     assert len(data_domain.patterns) == 1

    #     assert isinstance(data_domain.patterns[0], sample_pattern_class)
    #     assert data_domain.patterns[0].arg1 == "value1"
    #     assert data_domain.patterns[0].arg2 == "value2"
        
    #     print("Success: test_add_pattern")