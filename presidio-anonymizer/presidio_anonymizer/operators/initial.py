# presidio_anonymizer/operators/initial.py
from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """Minimal 'initial' anonymizer for tests."""

    def operate(self, text: str, params: Dict = None) -> str:
        """
        Perform the anonymization. Minimal behavior:
        - if params contains 'new_value' use that
        - otherwise return a visible default marker
        """
        params = params or {}
        return params.get("new_value", "[INITIAL]")

    def validate(self, params: Dict = None) -> None:
        """
        No required params for this minimal operator.
        If you need to enforce something later, add checks here.
        """
        return None

    def operator_name(self) -> str:
        """Return the operator name used for registration/lookups."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """This is an anonymize operator."""
        return OperatorType.Anonymize
