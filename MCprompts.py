from checks import checkBarcode # verify barcodes are numbers only and 46 digits
from MCjson import Payload # takes InventoryType, Barcode and LocationId
from colors import Color
from MoveCompletes import doMoveComplete # takes url and payload

def loadPlant():
    plant = ""

    print("SELECT TYPE:")
    print("     1) PORK")
    print("     2) BEEF")
    print("     3) EXIT")
    selection = input()

    if selection == "1":
        print("SELECT PLANT:")
        print("     1) Beardstown")
        print("     2) Louisville")
        print("     3) Marshalltown")
        print("     4) Ottumwa")
        print("     5) Pipestone")
        print("     6) Worthington")
        selection = input()
        if selection == "1":
            plant = "Beardstown"
        elif selection == "2":
            plant = "Louisville"
        elif selection == "3":
            plant = "Marshalltown"
        elif selection == "4":
            plant = "Ottumwa"
        elif selection == "5":
            plant = "Pipestone"
        elif selection == "6":
            plant = "Worthington"

    elif selection == "2":
        print("SELECT PLANT:")
        print("     1) Brooks")
        print("     2) Cactus")
        print("     3) Grand Island")
        print("     4) Greeley")
        print("     5) GVA")
        print("     6) Greenbay")
        print("     7) Hyrum")
        print("     8) Omaha")
        print("     9) Plainwell")
        print("     10) Souderton")
        print("     11) Tollseon")
        selection = input()
        if selection == "1":
            plant = "Brooks"
        elif selection == "2":
            plant = "Cactus"
        elif selection == "3":
            plant = "Grand Island"
        elif selection == "4":
            plant = "Greeley"
        elif selection == "5":
            plant = "GreeleyValueAdded"
        elif selection == "6":
            plant = "Greenbay"
        elif selection == "7":
            plant = "Hyrum"
        elif selection == "8":
            plant = "Omaha"
        elif selection == "9":
            plant = "Plainwell"
        elif selection == "10":
            plant = "Souderton"
        elif selection == "11":
            plant = "Tolleson"
    elif selection == "3":
        pass

    return plant

def loadPayload(url):
    payloadType = ""

    print("Type of movement?")
    print("     1) Case")
    print("     2) Pallet")

    selection = input()

    if selection == "1":
        payloadType = "C"
        print("Enter Barcodes: ('F' to finish)")
        barcodes = []
        entry = ""
        while entry != "F" and entry != "f":
            entry = input()
            if entry != "F" and entry != "f":
                if checkBarcode(entry):
                    barcodes.append(entry)
            else:
                break

        print("Enter Location to move to: (LAST STEP)")
        location = input()
        for i in barcodes:
            payload = Payload(payloadType, i, location)
            payload.to_json()

            status, statusCode, response = doMoveComplete(url, payload.data)
            if status:
                print(Color.BLUE, status, statusCode, response, Color.RESET)
            else:
                print(Color.RED, status, statusCode, response, Color.RESET)
    elif selection == "2":
        payloadType = "P"

        print("Enter Pallet ID:")
        pallet = input()
        print("Enter Location to move to: (LAST STEP)")
        location = input()

        payload = Payload(payloadType, pallet, location)
        payload.to_json()

        status, statusCode, response = doMoveComplete(url, payload.data)

        if status:
            print(Color.BLUE, status, statusCode, response, Color.RESET)
        else:
            print(Color.RED, status, statusCode, response, Color.RESET)

if __name__ == "__main__":
    print(Color.RED, "DO NOT RUN THIS SCRIPT DIRECTLY.", Color.RESET)