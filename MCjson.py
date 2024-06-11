import json
from colors import Color

class Payload:
    def __init__(self, InventoryType, Barcode, LocationId):
        self.data = {
            "InventoryType": InventoryType,
            "Barcode": Barcode,
            "LocationId": LocationId
            }
        
    def updateInventoryType(self, newValue):
        self.data["InventoryType"] = newValue

    def updateBarcode(self, newValue):
        self.data["Barcode"] = newValue

    def updateLocationId(self, newValue):
        self.data["LocationId"] = newValue
    
    def to_json(self):
        self = json.dumps(self.data)

if __name__ == "__main__":
    print(Color.RED, "DO NOT RUN THIS SCRIPT DIRECTLY.", Color.RESET)