#Tuples are immutable sequences that are used in loops with functions like zip, enumerate, and the dictionary method items().
#These return tuples that make looping over data easy. See my examples below:

# using zip() to loop over a list

cars = ['truck', 'van', 'sedan']
speeds = [85, 92, 78]
for cars, speed in zip(cars, speeds):
    print("example1:")
    print(f"{cars} has a speed of {speed}")

# Using enumerate() to track indices while looping
car_colors = ['red', 'green', 'blue']
for index, color in enumerate(car_colors):
    print("example2:")
    print(f"Car color at index {index} is {color}")

# items()
vehicles_inventory = {'cars': 10, 'trucks': 5, 'vans': 8}
for vehicles, quantity in vehicles_inventory.items():
    print("example3:")
    print(f"We have {quantity} {vehicles}")