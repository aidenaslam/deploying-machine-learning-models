from my_module import square
import pytest


# We can use parameterisation to test multiple inputs
@pytest.mark.parametrize(
    'inputs', [
        2, 3, 4
    ]
)
def test_square_return_value_type_is_int(inputs):
    # When
    subject = square(inputs)

    # Then
    assert isinstance(subject, int)

# Running pytest in anaconda prompt should run 5 tests in total:
# 1. my_test_module
# 2. my_test_module_again
# 3/4/5. test_paramterisation