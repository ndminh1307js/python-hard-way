# There are 100 cars
cars = 100
# There are 4 seats in each car
spaceInACar = 4.0
# There are 30 drivers and 90 passengers
drivers = 30
passengers = 90
# Number of cars with and without driver
carsNotDriven = cars - drivers
carsDriven = drivers
# The capacity of the cars
carpoolCapacity = carsDriven * spaceInACar
# The average of the passengers per car
averagePassengersPerCar = passengers / carsDriven

# Results
print('There are', cars, "cars available.")
print('There are only', drivers, 'drivers.')
print('There will be', carsNotDriven, 'empty cars today.')
print('We can transport', carpoolCapacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', averagePassengersPerCar, 'in each car.')
