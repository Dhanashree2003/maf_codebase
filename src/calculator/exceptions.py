class CalculatorError(Exception):
    """Base exception for calculator operations."""


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""