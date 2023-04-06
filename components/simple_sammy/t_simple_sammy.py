
import pytest
from typing import Any
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.testclient import TestClient

from your_module import SimpleSammy, NameInput, AdjectiveOutput, NameCombinationOutput


# Defining test cases for test_transform()
test_cases = [
    (
        {"name": "John"},
        {
            "adjective": "creative",
            "combined_name": "JohnCreative"
        }
    ),
    (
        {"name": "Alice"},
        {
            "adjective": "determined",
            "combined_name": "AliceDetermined"
        }
    )
]

# Using pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output_data", test_cases)
def test_transform(input_data: dict, expected_output_data: dict) -> None:

    # Create NameInput object from input_data dictionary
    name_input = NameInput(**input_data)

    # Create SimpleSammy object
    simple_sammy = SimpleSammy()

    # Call component's transform() method
    output_data = simple_sammy.transform(args=name_input, callbacks=None)

    # Unpack the output data tuple into AdjectiveOutput and NameCombinationOutput objects
    adjective_output, name_combination_output = output_data

    # Assert the output values match the expected_output_data
    assert adjective_output.adjective == expected_output_data["adjective"]
    assert name_combination_output.combined_name == expected_output_data["combined_name"]

def test_transform_edge_cases() -> None:
    # Test with empty input
    name_input = NameInput(name="")
    
    with pytest.raises(Exception):
        simple_sammy = SimpleSammy()
        simple_sammy.transform(args=name_input, callbacks=None)  # expect an exception to be raised

    # Test with long name input
    long_name = "a" * 500
    name_input = NameInput(name=long_name)

    with pytest.raises(Exception):
        simple_sammy = SimpleSammy()
        simple_sammy.transform(args=name_input, callbacks=None)  # expect an exception to be raised
