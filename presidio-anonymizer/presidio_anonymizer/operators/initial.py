# presidio_anonymizer/operators/initial.py
from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """Minimal 'initial' anonymizer for tests."""

    def operate(self, text: str, params: Dict = None) -> str:

        if not isinstance(text, str):
            return text

        # strip leading/trailing whitespace and split on any whitespace (collapses multiples)
        parts = [p for p in text.strip().split() if p]

        initials_list = []
        for part in parts:
            # Find first alphabetical character in the part (handles punctuation/hyphens)
            initial_char = None
            for ch in part:
                if ch.isalpha():
                    initial_char = ch
                    break
            if initial_char:
                initials_list.append(f"{initial_char.upper()}.")

        if not initials_list:
            # No alphabetic characters found — return original text unchanged
            return text

        return " ".join(initials_list)

    def validate(self, params: Dict = None) -> None:
        """No validation required for minimal operator."""
        return None

    def operator_name(self) -> str:
        """Return the operator name used for registration/lookups."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """This is an anonymize operator."""
        return OperatorType.Anonymize
