from my_module import square


# 01 - Initial test - run in anaconda prompt: pytest
# Test should pass
#def test_square_gives_correct_value():
    # When
 #   subject = square (2)

    # Then
  #  assert subject == 4

# 02 - Let's use a fixture instead
# Comment out lines 4-11 above
# import pytest
import pytest

# add decorator that has input value for the test
#@pytest.fixture
#def input_value():
    #return 4

def test_square_gives_correct_value(input_value):
    # When
    subject = square (input_value)

    # Then
    assert subject == 16

# 03 - Test for checking if value is int
# Note that we are usng the same fixture as before!
# Fixtures allow same values to be applied to different tests

#def test_square_return_value_type_is_int(input_value):
    # When
    #subject = square (input_value)

    # Then
    #assert isinstance(subject, int)

# 04 - Making use of fixtures with tests in different files
# Copy test_square_return_value_type_is_int into new file
# Comment out lines 19-21 and 34-39
# Copy the fixture across to the file conftest (this name is standard practice)

# Running pytest in anaconda prompt should run both tests with the inpit_values
# taken from the fixture saved in conftest.py