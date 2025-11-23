# presidio_anonymizer/operators/initial.py
from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """Minimal 'initial' anonymizer for tests."""

    def operate(self, text: str, params: Dict = None) -> str:
        """
        Convert a full name into initials.
        Examples:
            "John Smith" -> "J. S."
            "john   doe"  -> "J. D."
            "Mary-Jane O'Neil" -> "M. O."
            "Single" -> "S."
        Rules:
        - Split on whitespace, ignore empty parts.
        - For each name part, pick the first alphabetical character.
        - Uppercase the initial, append a period.
        - Join initials with a single space.
        """
        if not isinstance(text, str):
            return text

        # Split by whitespace and filter out empties
        parts = [p for p in text.strip().split() if p]

        initials_list = []
        for part in parts:
            # Find first alphabetical character in the part
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
