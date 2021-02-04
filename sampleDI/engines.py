"""Dependency injection example, engines module."""


class Engine:
    """Example engine base class.

    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """
    def __init__(self, engine):
        self.engine = engine

    def __repr__(self):
        return self.engine


class GasolineEngine(Engine):
    """Gasoline engine."""
    def __repr__(self):
        return 'gasoline engine'


class DieselEngine(Engine):
    """Diesel engine."""
    def __repr__(self):
        return 'diesel engine'


class ElectricEngine(Engine):
    """Electric engine."""
    def __init__(self):
        self.engine = 'electric engine'

    def __repr__(self):
        return self.engine
