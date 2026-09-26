from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class AuditEvent:
    status: str
    operation: str
    description: str
    timestamp: datetime


class AuditService:
    """
    Records successful and failed calculation events.
    """

    def __init__(self):
        self._events: list[AuditEvent] = []

    def log_success(
        self,
        operation: str,
        result: float,
    ) -> None:

        self._events.append(
            AuditEvent(
                status="SUCCESS",
                operation=operation,
                description=f"Calculation completed with result {result}",
                timestamp=datetime.now(timezone.utc),
            )
        )

    def log_failure(
        self,
        operation: str,
        reason: str,
    ) -> None:

        self._events.append(
            AuditEvent(
                status="FAILURE",
                operation=operation,
                description=reason,
                timestamp=datetime.now(timezone.utc),
            )
        )

    def get_events(self) -> list[AuditEvent\]:
        return list(self._events)