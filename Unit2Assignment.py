def print_circum(r):
    pi = 3.14159
    c = 2 * pi * r
    print(f"log: radius {r} has been recieved as arg.")
    print(f"Calculating circumference...")
    print(f"Circum = {c}")

# Calling the function with different values for radius
# print_circum(1)
# print_circum(10)
# print_circum(100)

# This shows that as the radius of the circle increases, the circumference also increases proportionally. 
# This is something that we all should be well aware of at this level of academia. 
# The circumference of a circle is directly proportional to the radius of the circle due to the fact that radius 
# is simple half the distance across a circle. Whereas circumference is the entire distance across

class MyUnit2StoreCatalog:
    def __init__(self):
        self.item1 = 200
        self.item2 = 400
        self.item3 = 600

    def get_price(self, item_list):
        price = 0

        if len(item_list) == 1:
            if item_list[0] == 1:
                price = self.item1
            elif item_list[0] == 2:
                price = self.item2
            elif item_list[0] == 3:
                price = self.item3
        elif len(item_list) == 2:
            if set(item_list) == {1, 2}:
                price = self.item1 + self.item2 - 0.1 * (self.item1 + self.item2)
            elif set(item_list) == {1, 3}:
                price = self.item1 + self.item3 - 0.1 * (self.item1 + self.item3)
            elif set(item_list) == {2, 3}:
                price = self.item2 + self.item3 - 0.1 * (self.item2 + self.item3)
        elif len(item_list) == 3:
            price = self.item1 + self.item2 + self.item3 - 0.25 * (self.item1 + self.item2 + self.item3)

        return price

catalog = MyUnit2StoreCatalog()

print("item 1:", catalog.get_price([1]))
print("item 2:", catalog.get_price([2])) 
print("item 3:", catalog.get_price([3]))
print("combo 1 (item 1 + item 2):", catalog.get_price([1, 2]))
print("combo 2 (item 2 + item 3):", catalog.get_price([2, 3])) 
print("combo 3 (item 1 + item 3):", catalog.get_price([1, 3]))
print("combo 4 (all items with 25% off order):", catalog.get_price([1, 2, 3]))