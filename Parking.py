# Create parking lot objects
# 1. Simulate a parking lot and the cars in it
#   - Have functions for each class appropriate to their hierarchy to interact with eachother

# Uppercase naming convention for classes
class Car:
    def __init__(self, color, model, licenses):
        self.color = color
        self.model = model
        self.licenses = licenses

    def __repr__(self):
        return f"{self.color}: {self.model} ({self.licenses})"


blue_car = Car("blue", "nissan versa", "FHJD7")
print(blue_car)


# "asd"  : String
# u"asd" : UnicodeString
# f"asd" : FormatString
# magic functions
# public vs private functions


class ParkingLot:
    def __init__(self, max_spots, parking_map=None):
        self.max_spots = max_spots
        if not parking_map:
            self.parking_map = self._populate_parking_map(max_spots)
        else:
            self.parking_map = parking_map

    def _populate_parking_map(self, max_spots):
        parking_map = {}
        for spot in range(max_spots):
            parking_map[spot] = None

        # self.parking_map = parking_map
        return parking_map

    def __repr__(self):
        return f"{self.max_spots}: {self.parking_map}"


# max_spots[1] = blue_car
#        {1: blue_car}
# parking_map = {'1': None, '2': None}
import ipdb;

ipdb.set_trace()
parking_lot = ParkingLot(2)
print(parking_lot)



