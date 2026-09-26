from calculator.validator import InputValidator
from calculator.history_service import HistoryService
from calculator.audit_service import AuditService
from calculator.exceptions import DivisionByZeroError


class Calculator:
    """
    Main calculation service.

    All arithmetic operations are validated, stored in history,
    and recorded in the audit service.
    """

    def __init__(
        self,
        validator: InputValidator,
        history_service: HistoryService,
        audit_service: AuditService,
    ):
        self.validator = validator
        self.history_service = history_service
        self.audit_service = audit_service

    def add(self, first: float, second: float) -> float:
        self.validator.validate_numbers(first, second)

        result = first + second

        self._record_calculation(
            operation="ADD",
            first=first,
            second=second,
            result=result,
        )

        return result

    def subtract(self, first: float, second: float) -> float:
        self.validator.validate_numbers(first, second)

        result = first - second

        self._record_calculation(
            operation="SUBTRACT",
            first=first,
            second=second,
            result=result,
        )

        return result

    def multiply(self, first: float, second: float) -> float:
        self.validator.validate_numbers(first, second)

        result = first * second

        self._record_calculation(
            operation="MULTIPLY",
            first=first,
            second=second,
            result=result,
        )

        return result

    def divide(self, first: float, second: float) -> float:
        self.validator.validate_numbers(first, second)

        if second == 0:
            self.audit_service.log_failure(
                operation="DIVIDE",
                reason="Division by zero attempted",
            )

            raise DivisionByZeroError(
                "Division by zero is not permitted."
            )

        result = first / second

        self._record_calculation(
            operation="DIVIDE",
            first=first,
            second=second,
            result=result,
        )

        return result

    def _record_calculation(
        self,
        operation: str,
        first: float,
        second: float,
        result: float,
    ) -> None:

        self.history_service.save(
            operation=operation,
            first=first,
            second=second,
            result=result,
        )

        self.audit_service.log_success(
            operation=operation,
            result=result,
        )