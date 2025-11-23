# presidio_anonymizer/operators/initial.py
from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """Minimal 'initial' anonymizer for tests."""

    def operate(self, text: str, params: Dict = None) -> str:
        if not isinstance(text, str):
            return text

        parts = [p for p in text.strip().split() if p]
        initials_list = []

        for part in parts:
            # find index of first alphanumeric character
            idx = None
            for i, ch in enumerate(part):
                if ch.isalnum():
                    idx = i
                    break

            if idx is None:
                # no alphanumeric char in this part -> skip it
                continue

            prefix = part[:idx]  # everything before the alphanumeric char
            alnum_char = part[idx]
            # uppercase if it's a letter; digits unchanged
            initial_char = alnum_char.upper() if alnum_char.isalpha() else alnum_char
            initials_list.append(f"{prefix}{initial_char}.")

        if not initials_list:
            # If we didn't find any alphanumeric characters at all, return original text
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
