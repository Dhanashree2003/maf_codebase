import pytest

from calculator.calculator import Calculator
from calculator.validator import InputValidator
from calculator.history_service import HistoryService
from calculator.audit_service import AuditService
from calculator.exceptions import DivisionByZeroError


@pytest.fixture
def calculator():
    return Calculator(
        validator=InputValidator(),
        history_service=HistoryService(),
        audit_service=AuditService(),
    )


def test_add(calculator):
    assert calculator.add(10, 5) == 15


def test_subtract(calculator):
    assert calculator.subtract(10, 5) == 5


def test_multiply(calculator):
    assert calculator.multiply(10, 5) == 50


def test_divide(calculator):
    assert calculator.divide(10, 5) == 2


def test_divide_by_zero(calculator):
    with pytest.raises(DivisionByZeroError):
        calculator.divide(10, 0)


def test_successful_operation_saved_in_history(calculator):
    calculator.add(10, 5)

    history = calculator.history_service.get_history()

    assert len(history) == 1
    assert history[0].operation == "ADD"
    assert history[0].result == 15


def test_successful_operation_is_audited(calculator):
    calculator.multiply(4, 5)

    events = calculator.audit_service.get_events()

    assert len(events) == 1
    assert events[0].status == "SUCCESS"


def test_invalid_large_value_rejected(calculator):
    with pytest.raises(ValueError):
        calculator.add(2_000_000, 10)