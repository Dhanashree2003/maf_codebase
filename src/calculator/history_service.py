from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class CalculationRecord:
    operation: str
    first: float
    second: float
    result: float
    timestamp: datetime


class HistoryService:
    """
    Stores successful calculation history.

    This implementation uses an in-memory list for the sample project.
    It can later be replaced with database persistence.
    """

    def __init__(self):
        self._records: list[CalculationRecord] = []

    def save(
        self,
        operation: str,
        first: float,
        second: float,
        result: float,
    ) -> None:

        record = CalculationRecord(
            operation=operation,
            first=first,
            second=second,
            result=result,
            timestamp=datetime.now(timezone.utc),
        )

        self._records.append(record)

    def get_history(self) -> list[CalculationRecord\]:
        return list(self._records)

    def clear_history(self) -> None:
        self._records.clear()