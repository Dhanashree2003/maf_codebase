class InputValidator:
    """
    Validates inputs before arithmetic operations are executed.
    """

    MAX_ABSOLUTE_VALUE = 1_000_000

    def validate_numbers(
        self,
        first: float,
        second: float,
    ) -> None:

        if not isinstance(first, (int, float)):
            raise TypeError("First value must be numeric.")

        if not isinstance(second, (int, float)):
            raise TypeError("Second value must be numeric.")

        if abs(first) > self.MAX_ABSOLUTE_VALUE:
            raise ValueError(
                "First value exceeds the supported calculation limit."
            )

        if abs(second) > self.MAX_ABSOLUTE_VALUE:
            raise ValueError(
                "Second value exceeds the supported calculation limit."
            )