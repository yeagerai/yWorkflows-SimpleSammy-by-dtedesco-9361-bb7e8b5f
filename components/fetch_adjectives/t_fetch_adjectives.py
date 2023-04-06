
import pytest
from pydantic import BaseModel
from fastapi.testclient import TestClient
from my_component.fetch_adjectives import (
    FetchAdjectives,
    FetchAdjectivesInputDict,
    FetchAdjectivesOutputDict,
    fetch_adjectives_app,
)

# A list of test cases with mocked input and expected output data
test_cases = [
    {
        "input": FetchAdjectivesInputDict(),
        "expected_output": FetchAdjectivesOutputDict(
            adjective_list={
                "a": ["awesome", "amazing"],
                "b": ["brave", "blissful"],
                # Add more letters and corresponding adjectives as needed
            }
        ),
    },
    # Add more test cases as needed
]

client = TestClient(fetch_adjectives_app)


# Create multiple test scenarios using parameterized test cases
@pytest.mark.parametrize("test_case", test_cases)
def test_fetch_adjectives(test_case):
    # Mock the fetch_adjectives method to return predetermined adjectives
    def mock_fetch_adjectives(self, letter: str) -> list[str]:
        test_adjectives = {
            "a": ["awesome", "amazing"],
            "b": ["brave", "blissful"],
            # Add more letters and corresponding adjectives as needed
        }
        return test_adjectives[letter]

    FetchAdjectives.fetch_adjectives = mock_fetch_adjectives

    # Call the component's transform method and compare the output to the expected result
    fetch_adjectives = FetchAdjectives()
    output = fetch_adjectives.transform(test_case["input"])
    assert output == test_case["expected_output"]

    # Test FastAPI route
    response = client.post("/transform/", json=test_case["input"].dict())
    assert response.status_code == 200
    assert response.json() == test_case["expected_output"].dict()
