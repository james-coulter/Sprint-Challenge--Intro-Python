# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # <-- Base
    pass


class FlightVehicle(Vehicle):  # <-- parent class to airplane
    pass


class Starship(FlightVehicle):
    pass


class GroundVehicle(Vehicle):  # <-- parent class to Car and Motorcycle
    pass


class Airplane(FlightVehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

