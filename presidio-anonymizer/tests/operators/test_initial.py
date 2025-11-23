# tests/operators/test_initial.py
import pytest
from presidio_anonymizer.operators.initial import Initial


def test_correct_name():
    assert Initial().operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("     Eastern    Michigan   University ", "E. M. U."),
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    assert Initial().operate(input_text) == initials
