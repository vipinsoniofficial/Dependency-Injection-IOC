"""Dependency injection example, cars module."""


class Car:
    """Example car."""

    def __init__(self, engine):
        """Initializer."""
        self.engine = engine  # Engine is injected

    def __repr__(self):
        return self.engine
