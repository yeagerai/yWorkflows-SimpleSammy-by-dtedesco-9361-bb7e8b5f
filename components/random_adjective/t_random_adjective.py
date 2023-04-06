
import pytest
from pydantic import ValidationError
from core.random_adjective import RandomAdjective, RandomAdjectiveInputDict, RandomAdjectiveOutputDict

# Define test cases with mocked input and expected output data.
test_data = [
    (
        RandomAdjectiveInputDict({"adjective_list": ["apple", "banana"], "name": "Alice"}),
        RandomAdjectiveOutputDict({"adjective": "apple"}),
    ),
    (
        RandomAdjectiveInputDict({"adjective_list": ["grape", "lime"], "name": "George"}),
        RandomAdjectiveOutputDict({"adjective": "grape"}),
    ),
    (
        RandomAdjectiveInputDict({"adjective_list": ["apple", "banana"], "name": "Zeke"}),
        None,
        ValueError("No adjectives found starting with the letter z"),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios.
@pytest.mark.parametrize("input_data,expected_output,error", test_data)
def test_random_adjective(input_data: RandomAdjectiveInputDict, expected_output: RandomAdjectiveOutputDict, error):
    random_adjective = RandomAdjective()
    
    # Write a test function that takes the mocked input, calls the component's transform() method,
    # and asserts that the output matches the expected output.
    if error:
        with pytest.raises(error):
            output_data = random_adjective.transform(input_data)
    else:
        output_data = random_adjective.transform(input_data)
        assert output_data == expected_output


# Test validation error for when the name is not provided
def test_invalid_input():
    with pytest.raises(ValidationError):
        RandomAdjectiveInputDict({"adjective_list": ["apple"]})
