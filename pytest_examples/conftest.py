# Fixture from conftest will be made available to all tests

import pytest

@pytest.fixture
def input_value():
    return 4