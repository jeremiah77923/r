class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    def set_ingridents(self,choice):
        """Sets the ingriedents of the machine"""
        ingredients = {"water": 0, "milk": 0, "coffee": 0}
        if self.set_choice(choice=choice) == 0:
            ingredients["water"] = 200
            ingredients["milk"] = 150
            ingredients["coffee"] = 24
        if self.set_choice(choice=choice) == 1:
            ingredients["water"] = 50
            ingredients["milk"] = 0
            ingredients["coffee"] = 18
        if self.set_choice(choice=choice) == 2:
            ingredients["water"] = 250
            ingredients["milk"] = 50
            ingredients["coffee"] = 24
        return ingredients
    def set_choice(self,choice):
        "returns t"
        index = 0
        if choice == "e":
            index = 1
        elif choice == "l":
            index = 0
        elif choice == "c":
            index = 2
        return index
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            if item != self.menu[len(self.menu)-1]:
                options += f"{item.name} cost: ${item.cost}, "
            if item == self.menu[len(self.menu) - 1]:
                options += f"{item.name} cost: ${item.cost}."
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
