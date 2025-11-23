from presidio_anonymizer.operators.initial import Initial
import pytest

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text) == initials
    assert text == initials