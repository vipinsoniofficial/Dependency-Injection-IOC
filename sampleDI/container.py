"""Dependency injection sampleDI, Cars & Engines IoC containers."""

import sampleDI.cars
import sampleDI.engines

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Engines(containers.DeclarativeContainer):
    """IoC container of engine providers."""

    gasoline = providers.Factory(sampleDI.engines.GasolineEngine)

    diesel = providers.Factory(sampleDI.engines.DieselEngine)

    electric = providers.Factory(sampleDI.engines.ElectricEngine)


class Cars(containers.DeclarativeContainer):
    """IoC container of car providers."""

    gasoline = providers.Factory(sampleDI.cars.Car,
                                 engine=Engines.gasoline)

    diesel = providers.Factory(sampleDI.cars.Car,
                               engine=Engines.diesel)

    electric = providers.Factory(sampleDI.cars.Car,
                                 engine=Engines.electric)


if __name__ == '__main__':
    gasoline_car = Cars.gasoline()
    diesel_car = Cars.diesel()
    electric_car = Cars.electric()
