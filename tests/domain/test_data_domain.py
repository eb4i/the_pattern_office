import pytest
from tpo.domain.data_domain import DataDomain

def test_data_domain_creation():
    data_domain = DataDomain(
        name="domain_name",
        abbreviation="domain_abbrev",
        zone="zone_name",
        description="Test Description",
        location="Global",
        owner={"name": "owner_name", "email": "owner_email"},
        tags=["tag1", "tag2"],
    )

    assert data_domain.name == "domain_name"
    assert data_domain.abbreviation == "domain_abbrev"
    assert data_domain.zone == "zone_name"
    assert data_domain.description == "Test Description"
    assert data_domain.location == "Global"
    assert data_domain.owner == {"name": "owner_name", "email": "owner_email"}
    assert data_domain.tags == ["tag1", "tag2"]

def test_add_pattern():
    data_domain = DataDomain(
        name="domain_name",
        abbreviation="domain_abbrev",
        zone="zone_name",
        description="Test Description",
        location="Global",
        owner={"name": "owner_name", "email": "owner_email"},
        tags=["tag1", "tag2"],
    )

    data_domain.add_pattern("pattern1")
    assert data_domain.patterns == ["pattern1"]

    data_domain.add_pattern("pattern2")
    assert data_domain.patterns == ["pattern1", "pattern2"]

def test_add_data_product():
    data_domain = DataDomain(
        name="domain_name",
        abbreviation="domain_abbrev",
        zone="zone_name",
        description="Test Description",
        location="Global",
        owner={"name": "owner_name", "email": "owner_email"},
        tags=["tag1", "tag2"],
    )

    data_domain.add_data_product("data_product1")
    assert data_domain.data_products == ["data_product1"]

    data_domain.add_data_product("data_product2")
    assert data_domain.data_products == ["data_product1", "data_product2"]
