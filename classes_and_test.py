# Problem for Prof Charnesky's mid term review sheet at:
# https://canvas.umd.umich.edu/courses/522665/pages/midterm-practice?module_item_id=9243802
# 1 Classes and Unit Test question
# Given the following UML, write the class
# Pizza
# toppings : []
# slices : int
# base_cost : float
# price_per_topping : int
# get_total_price() : int
# Write a unit test for get_total_price()
class Pizza:
    def __init__(self, toppings, slices, base_cost=2.5, price_per_topping=1):
        self._toppings = toppings
        self._slices = slices
        self._base_cost = base_cost
        self._price_per_topping = price_per_topping

    def get_total_price(self):
        return (self._base_cost + self._price_per_topping * (len(self._toppings))) * self._slices


if __name__ == "__main__":
    nice = Pizza(['pineapple', 'ham', 'mushrooms'], 3)
    print(nice.get_total_price())