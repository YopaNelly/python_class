"""
define a set of abstract classes and 
interfaces that will be used by multiple
 rental car companies, each of which may 
 have different types of cars and rental policies.
"""

from abc import ABC, abstractmethod

# Define an abstract class "Vehicle" that represents a rental vehicle
class Vehicle(ABC):
    # Define the constructor to initialize the make, model, and year of the vehicle
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Define an abstract method "get_rental_rate()" that returns the daily rental rate of the vehicle
    @abstractmethod
    def get_rental_rate(self):
        pass

# Define an abstract class "RentalPolicy" that represents a rental policy for a vehicle
class RentalPolicy(ABC):
    # Define an abstract method "get_daily_rate()" that returns the daily rental rate of the policy
    @abstractmethod
    def get_daily_rate(self):
        pass

    # Define an abstract method "get_mileage_limit()" that returns the maximum mileage allowed by the policy
    @abstractmethod
    def get_mileage_limit(self):
        pass

# Define a concrete class "CompactCar" that represents a compact rental car
class CompactCar(Vehicle):
    # Define an implementation of the "get_rental_rate()" method for the compact car
    def get_rental_rate(self):
        return 30.0

# Define a concrete class "StandardCar" that represents a standard rental car
class StandardCar(Vehicle):
    # Define an implementation of the "get_rental_rate()" method for the standard car
    def get_rental_rate(self):
        return 40.0

# Define a concrete class "UnlimitedRentalPolicy" that represents an unlimited rental policy
class UnlimitedRentalPolicy(RentalPolicy):
    # Define an implementation of the "get_daily_rate()" method for the unlimited policy
    def get_daily_rate(self):
        return 20.0

    # Define an implementation of the "get_mileage_limit()" method for the unlimited policy
    def get_mileage_limit(self):
        return float("inf")

# Define a concrete class "LimitedRentalPolicy" that represents a limited rental policy
class LimitedRentalPolicy(RentalPolicy):
    # Define the constructor to initialize the daily rate and mileage limit of the policy
    def __init__(self, daily_rate, mileage_limit):
        self.daily_rate = daily_rate
        self.mileage_limit = mileage_limit

    # Define an implementation of the "get_daily_rate()" method for the limited policy
    def get_daily_rate(self):
        return self.daily_rate

    # Define an implementation of the "get_mileage_limit()" method for the limited policy
    def get_mileage_limit(self):
        return self.mileage_limit

# Define a rental car company "ACMECarRentals" that rents out standard cars with unlimited policies
class ACMECarRentals:
    # Define the constructor to initialize the rental vehicle and policy of the company
    def __init__(self):
        self.vehicle = StandardCar("Ford", "Fusion", 2018)
        self.policy = UnlimitedRentalPolicy()

    # Define a method "get_daily_rate()" that returns the daily rental rate of the policy
    def get_daily_rate(self):
        return self.policy.get_daily_rate()

    # Define a method "get_mileage_limit()" that returns the maximum mileage allowed by the policy
    def get_mileage_limit(self):
        return self.policy.get_mileage_limit()

# Define a rental car company "XYZCarRentals" that rents out compact cars with limited policies
class XYZCarRentals:
    # Define the constructor to initialize the rental vehicle and policy of the company
    def __init__(self):
        self.vehicle = CompactCar("Toyota", "Camry", 2020)
        self.policy = LimitedRentalPolicy(25.0, 100)

    # Define a method "get_daily_rate()" that returns the daily rental rate of the policy
    def get_daily_rate(self):
        return self.policy.get_daily_rate()

    # Define a method "get_mileage_limit()" that returns the maximum mileage allowed by the policy
    def get_mileage_limit(self):
        return self.policy.get_mileage_limit()

# Create instances of the rental car companies
acme_rentals = ACMECarRentals()
xyz_rentals = XYZCarRentals()

# Call the methods of the rental car companies to get the rental rates and mileage limits
print(acme_rentals.vehicle.get_rental_rate())         # Output: 40.0
print(acme_rentals.get_daily_rate())                  # Output: 20.0
print(acme_rentals.get_mileage_limit())               # Output: inf

print(xyz_rentals.vehicle.get_rental_rate())          # Output: 30.0
print(xyz_rentals.get_daily_rate())                   # Output: 25.0
print(xyz_rentals.get_mileage_limit())                # Output: 100
