# tests/test_pattern_factory.py

import pytest
from tpo.pattern_factory import PatternFactory

@pytest.fixture
def pattern_factory():
    return PatternFactory()

@pytest.fixture
def sample_pattern_class():
    class SamplePattern:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    return SamplePattern

def test_register_and_create_pattern(pattern_factory, sample_pattern_class):
    pattern_factory.register_pattern("Sample", sample_pattern_class)
    pattern = pattern_factory.create_pattern("Sample", "value1", "value2")

    assert isinstance(pattern, sample_pattern_class)
    assert pattern.arg1 == "value1"
    assert pattern.arg2 == "value2"
    
    print("Success: test_register_and_create_pattern")
