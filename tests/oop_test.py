import pytest
import os
import sys
import inspect
import pdb

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import oop as OOP_Module

with open(currentdir + '/../oop.py', 'r') as myfile:
    file_data = myfile.read().replace('\n', '')

# mocks
vehicle_dict_vehicle = {
    "vehicle_type": "Vehicle",
    "wheel_count": 'no wheels!',
    "mpg": {
        "city": 19,
        "highway": 30,
        "combined": 27
    },
    "name": "A Laptop",
}

vehicle_dict_vehicle_2 = {
    "vehicle_type": "Vehicle",
    "wheel_count": 2,
    "mpg": {
        "city": 19,
        "highway": 30,
        "combined": 27
    },
    "name": "A Laptop",
}

vehicle_dict_car = {
    "vehicle_type": "Car",
    "wheel_count": 4,
    "mpg": {
        "city": 35,
        "highway": 50,
        "combined": 47
    },
    "name": "Mustang Grande",
}

vehicle_dict_motorcycle = {
    "vehicle_type": "Motorcycle",
    "wheel_count": 2,
    "mpg": {
        "city": 46,
        "highway": 70,
        "combined": 67
    },
    "name": "Ninja2"
}

vehicle_dict_motorcycle_2 = {
    "vehicle_type": "Motorcycle",
    "wheel_count": 3,
    "mpg": {
        "city": 46,
        "highway": 70,
        "combined": 67
    },
    "name": "Ninja2"
}
vehicle_dict_truck = {
    "vehicle_type": "Truck",
    "wheel_count": 8,
    "mpg": {
        "city": 45,
        "highway": 50,
        "combined": 55
    },
    "name": "Explorer"
}


# # TEST AS STRING
# def test_file_as_string0():
#     assert "class Car" in file_data, "the oop file does not contain the class `Car`"
#     assert "class Car(Vehicle):" in file_data, "Car does not inherit from Vehicle"

# def test_file_as_string1():
#     assert "def can_drive(self):" in file_data, 'you need to create the can_drive method in the car class'

# def test_file_as_string2():
#     assert "def __init__" in file_data, "each class needs an initialization method"
#     assert "self.wheel_count" in file_data, "each class should have the wheel_count property"

def test_vehicle_properties():
    v = OOP_Module.Vehicle(vehicle_dict_vehicle)
    assert v.vehicle_type == vehicle_dict_vehicle['vehicle_type'], 'Vehicle class: vehicle_type is incorrect'
    assert v.wheel_count == vehicle_dict_vehicle['wheel_count'], 'Vehicle class: wheel_count is incorrect'
    assert v.mpg['city'] == vehicle_dict_vehicle['mpg']['city'], 'Vehicle class: city mpg is incorrect'
    assert v.mpg['highway'] == vehicle_dict_vehicle['mpg']['highway'], 'Vehicle class: highway mpg is incorrect'
    assert v.mpg['combined'] == vehicle_dict_vehicle['mpg']['combined'], 'Vehicle class: combined mpg is incorrect'
    assert v.name == vehicle_dict_vehicle['name'], 'Vehicle class: name is incorrect'
    
def test_vehicle_methods():
    v = OOP_Module.Vehicle(vehicle_dict_vehicle)
    v_two = OOP_Module.Vehicle(vehicle_dict_vehicle_2)
    assert v.get_vehicle_type() == v.vehicle_type, "Vehicle class method get_vehicle_type() is returning an incorrect property"
    assert v.get_vehicle_drive() == 'no wheels send it back to the shop', "Vehicle class method get_vehicle_drive() is returning an incorrect property"
    assert v_two.get_vehicle_drive() == f"I have {v_two.wheel_count} wheel drive", "Vehicle class method get_vehicle_drive() should return a string that says 'I have {wheel_count} wheel drive'"

def test_truck_class_exists():
    assert hasattr(OOP_Module, 'Truck'), "the oop file does not contain a Truck class"

def test_car_class_exists():
    assert hasattr(OOP_Module, 'Car'), "the oop file does not contain a Car class"

def test_motorcycle_class_exists():
    assert hasattr(OOP_Module, 'Motorcycle'), "the oop file does not contain a Motorcycle class"

truck = None
motorcycle2 = None
motorcycle = None
car = None

if hasattr(OOP_Module, 'Truck'):
    truck = OOP_Module.Truck(vehicle_dict_truck)
if hasattr(OOP_Module, 'Car'):
    car = OOP_Module.Car(vehicle_dict_car) 
if hasattr(OOP_Module, 'Motorcycle'):
    motorcycle = OOP_Module.Motorcycle(vehicle_dict_motorcycle) 
    motorcycle2 = OOP_Module.Motorcycle(vehicle_dict_motorcycle_2) 

# TEST INHERITANCE OF CLASSES
def test_inheritance():
    assert OOP_Module.Car.__bases__[
        0] == OOP_Module.Vehicle, "the class 'Car' does not inherit from the 'Vehicle' class"
    assert OOP_Module.Truck.__bases__[
        0] == OOP_Module.Vehicle, "the class 'Truck' does not inherit from the 'Vehicle' class"
    assert OOP_Module.Motorcycle.__bases__[
        0] == OOP_Module.Vehicle, "the class 'Motorcycle' does not inherit from the 'Vehicle' class"

# CAR Datatypes
def test_car_data_types0():
    assert type(
        car.vehicle_type) == str, "the car.vehicle_type data type is wrong"
    assert type(car.wheel_count) == int, "the car.wheel_count data type is wrong"
    assert type(car.mpg["city"]
                ) == int, "the car.mpg['city'] data type is wrong"
    assert type(car.mpg["highway"]
                ) == int, "the car.mpg['highway'] data type is wrong"

def test_car_data_types1():
    assert type(car.mpg["combined"]
                ) == int, "the car.mpg['combined'] data type is wrong"
    assert type(car.name) == str, "the car.name data type is wrong"

# TEST CAR METHODS
def test_car_can_drive():
    assert car.can_drive() == "Vrrooooom Vroooom", "the car class 'can_drive' is not returning 'Vrrooooom Vroooom'"

# MOTORCYCLE Datatypes
def test_motorcycle_data_types0():
    assert type(
        motorcycle.vehicle_type) == str, "the motorcycle.vehicle_type data type is wrong"
    assert type(
        motorcycle.wheel_count) == int, "the motorcycle.wheel_count data type is wrong"
    assert type(
        motorcycle.mpg["city"]) == int, "the motorcycle.mpg['city'] data type is wrong"
    assert type(
        motorcycle.mpg["highway"]) == int, "the motorcycle.mpg['highway'] data type is wrong"
    assert type(motorcycle.mpg["combined"]
                ) == int, "the motorcycle.mpg['combined'] data type is wrong"


def test_motorcycle_data_types1():
    assert type(motorcycle.name) == str, "the motorcycle.name data type is wrong"

# TEST MOTORCYCLE METHODS


def test_motorcycle_methods():
    assert motorcycle.pop_wheelie() == "popped a wheelie!", "the motorcycle class method pop_wheelie is not returning 'popped a wheelie!' if the wheel count is 2 "
    assert motorcycle2.pop_wheelie() == False, "the motorcycle class method pop_wheelie should return False if the wheel count is not 2"

# TRUCK Data Types
def test_truck_data_types0():
    assert type(
        truck.vehicle_type) == str, "the truck.vehicle_type data type is wrong"
    assert type(
        truck.wheel_count) == int, "the truck.wheel_count data type is wrong"
    assert type(truck.mpg["city"]
                ) == int, "the truck.mpg['city'] data type is wrong"
    assert type(truck.mpg["highway"]
                ) == int, "the truck.mpg['highway'] data type is wrong"
    assert type(truck.mpg["combined"]
                ) == int, "the truck.mpg['combined'] data type is wrong"


def test_truck_data_types1():
    assert type(truck.name) == str, "the truck.name data type is wrong"

    # TEST TRUCK METHODS


def test_truck_methods():
    assert truck.rev_engine(
    ) == "rreevv!", "the truck classes method rev_engine is not returning 'rreevv!' "
